import sys
from subprocess import Popen, PIPE
from CodeforcesComms import CodeforcesComms
from Parser import Parser

DIVIDER = "-------------------------------------------------------------------------"

class CodeforcesCLI(object):
    """Main cli class"""
    def __init__(self, file_location, lang = "c++", compiler = "c++"):
        self.file_location = file_location
        self.file_name = None
        self.file_extn = None
        self.file_output = None
        self.file_output_extn = None
        self.lang = lang
        self.compiler = compiler
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

        file_name_start = len(self.file_location) - 1
        while(self.file_location[file_name_start] != '/' and file_name_start != -1):
            file_name_start -= 1

        file_name_start += 1
        self.file_name = self.file_location[file_name_start : self.file_location.find(".", file_name_start)]
        self.file_extn = self.file_location[self.file_location.find(".", file_name_start) + 1 : ]

        contest_id_end = len(self.file_name) - 1

        self.contest_id = self.file_name[ :contest_id_end]
        self.problem_id = self.file_name[contest_id_end: contest_id_end + 1]

        self.file_output = self.file_name + self.file_output_extn

        return 0

    def compile(self):

        print DIVIDER
        print "Compiling " + self.file_location + " using " + self.compiler

        compilation = Popen([self.compiler, self.file_location,  "-o", self.file_output])
        compilation_output = compilation.communicate()

        if compilation.returncode == 0:
            print "Compilation successful!"
            print "Output file: " + self.file_output

        print DIVIDER

        return compilation.returncode

    def run_all_test_cases(self):

        pass_count = 0

        for case in self.test_cases:
            print "./" + self.file_output
            proc = Popen(["./" + self.file_output], stdout = PIPE, stdin = PIPE)
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

        if(pass_count == len(self.test_cases)):
            return 0
        else:
            return 1

    def fetch_test_cases(self):

        if self.file_name == None:
            self.parse_file_name()

        print "\nFetching test cases for problem " + self.contest_id + self.problem_id
        page = self.comms.open_problem_page(self.contest_id, self.problem_id)
        self.test_cases = self.parser.get_test_cases(page)
        print "Test cases fetching successful."

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
        self.parse_file_name()
        self.compile()
        self.fetch_test_cases()
        #self.write_test_cases_to_file()
        self.run_all_test_cases()

        return 0
