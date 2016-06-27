import sys
import os
from subprocess import Popen, PIPE
from CodeforcesComms import CodeforcesComms
from Parser import Parser

DIVIDER = "-------------------------------------------------------------------------"


class CodeforcesCLI(object):
    """Main cli class"""

    def __init__(self, compiler, file_location, compiler_options = "", lang = "c++"):
        self.file_location = file_location
        self.file_name = None
        self.file_extn = None
        self.file_output_name = None    #Includes output file extension
        self.file_output_extn = None
        self.lang = lang
        self.compiler = compiler
        self.compiler_options = compiler_options
        self.test_cases = []            #Each test case is a pair [input, output]
        self.test_case_files = []
        self.contest_id = None
        self.problem_id = None
        self.comms = CodeforcesComms()
        self.parser = Parser()

        if(lang == "c++"):
            self.file_output_extn = ".out"

    def __config_comms(self, username = None, password = None):
        self.comms.contest_id = str(self.contest_id)
        self.comms.problem_id = str(self.problem_id)
        self.comms.username = username
        self.comms.password = password

    def parse_file_name(self):

        try:
            file_name_start = self.file_location.rfind('/') + 1

            self.file_name = self.file_location[file_name_start : self.file_location.rfind('.')]
            self.file_extn = self.file_location[self.file_location.find(".", file_name_start) + 1 : ]

            contest_id_end = len(self.file_name) - 1

            self.contest_id = self.file_name[ :contest_id_end]
            self.problem_id = self.file_name[contest_id_end: contest_id_end + 1]

            if(not self.problem_id.isalpha()):
                self.problem_id = ""

            if 0 in [len(self.file_name), len(self.contest_id), len(self.problem_id)]:
                raise

            self.file_output_name = self.file_name + self.file_output_extn

        except:
            raise RuntimeError("Looks like you are using wrong filename format. Correct examples: 308a.cpp, 668b.py")
            return 1

    def compile(self):
        try:
            print DIVIDER
            print "Compiling " + self.file_name + "." + self.file_extn + " using " + self.compiler + " and options" + self.compiler_options

            if len(self.compiler_options) > 0:
                compilation = Popen([self.compiler, self.file_location,  "-o", self.file_output_name, self.compiler_options])
            else:
                compilation = Popen([self.compiler, self.file_location,  "-o", self.file_output_name])

            compilation_output = compilation.communicate()

            if compilation.returncode == 0:
                print "Compilation successful!"
                print "Output file: " + os.path.dirname(os.path.abspath(__file__)) + "/" + self.file_output_name

            else:
                raise RuntimeError("error")

            print DIVIDER

            return compilation.returncode

        except:
            raise RuntimeError("Error compiling your code.")
            return 1


    def run_all_test_cases(self):

        #Return codes:
        # 0 - successful
        # 1 - Wrong Answer
        # 2 - Error executing

        try:
            pass_count = 0

            for case in self.test_cases:
                proc = Popen(["./" + self.file_output_name], stdout = PIPE, stdin = PIPE)
                out = proc.communicate(case[0].strip())
                print "Input: "
                print case[0].strip()
                print "\nOutput: "
                print out[0].strip()
                print "\nExpected Output: "
                print case[1].strip()

                if(out[0].strip() == case[1].strip()):
                    print "\nVerdict: Pass"
                    pass_count += 1
                else:
                    print "\nVerdict: Fail"

                print DIVIDER

            print str(pass_count) + " of " + str(len(self.test_cases)) + " test cases Match."
            print DIVIDER

            if(pass_count != len(self.test_cases)):
                raise RuntimeError("Wrong answer")

            return 0

        except RuntimeError:
             RuntimeError("Error executing test cases.")
             return 1

        except OSError:
            RuntimeError("Error executing the program")

    def fetch_test_cases(self):

        try:
            if self.file_name == None:
                self.parse_file_name()

            print "\nFetching test cases for problem " + self.contest_id + self.problem_id
            page = self.comms.open_problem_page(self.contest_id, self.problem_id)
            self.test_cases = self.parser.get_test_cases(page)
            print "Test cases fetching successful."

        except:
            raise RuntimeError("Error fetching test cases.")

    def write_test_cases_to_file(self):
        print "Saving test cases..."
        folder_name = self.contest_id + self.problem_id + "_testcases/"

        #check if directory already exists
        proc = Popen(['find', folder_name], shell = False, stdout = PIPE, stderr = PIPE)
        if proc.communicate()[0] != folder_name[:-1]:
            Popen(['mkdir', folder_name], shell = False, stdout = PIPE, stderr = PIPE)

        for case, i in zip(self.test_cases, range(0, len(self.test_cases))):
            f = open(folder_name + str(i) + ".in", "w+")
            f.write(case[0])
            f = open(folder_name + str(i) + ".out", "w+")
            f.write(case[1])
            f.close()

            self.test_case_files.append([folder_name + str(i) + ".in", folder_name + str(i) + ".out"])

        print "Test cases saved."
        print DIVIDER

    def run(self):
        try:
            self.parse_file_name()
            self.compile()
            self.fetch_test_cases()
            #self.write_test_cases_to_file()
            self.run_all_test_cases()
        except RuntimeError as e:
            print e
            return 1
        except OSError as e:
            print
            return 1

        return 0
