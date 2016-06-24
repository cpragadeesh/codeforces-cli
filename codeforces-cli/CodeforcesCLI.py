import sys
from subprocess import Popen, PIPE
from CodeforcesComms import CodeforcesComms
from Parser import Parser

DIVIDER = "----------------------------------------------------------------------"

class CodeforcesCLI(object):
    """Main cli class"""
    def __init__(self, file_name, lang = "c++", compiler = "c++"):
        self.file_name = file_name
        self.lang = lang
        self.compiler = compiler
        self.test_cases = []            #Each test case is a pair [input, output]
        self.test_case_files = []
        self.contest_id = None
        self.problem_id = None
        self.comms = CodeforcesComms()
        self.parser = Parser()

    def __config_comms(self, username = None, password = None):
        self.comms.contest_id = str(self.contest_id)
        self.comms.problem_id = str(self.problem_id)
        self.comms.username = username
        self.comms.password = password

    def __parse_file_name(self):

        contest_id_end = self.file_name.find(".")
        contest_id_end = contest_id_end - 1

        self.contest_id = self.file_name[ :contest_id_end]
        self.problem_id = self.file_name[contest_id_end: contest_id_end + 1]

        self.__config_comms()

        return 0

    def compile(self):

        print DIVIDER
        print "Compiling " + self.file_name + " using " + self.compiler
        compilation = Popen([self.compiler, self.file_name])
        compilation_output = compilation.communicate()

        if compilation.returncode == 0:
            print "Compilation successful!"

        print DIVIDER

        return compilation.returncode

    def run_all_test_cases(self):
        pass

    def fetch_test_cases(self):
        self.__parse_file_name()
        print "\nFetching test cases for problem " + self.contest_id + self.problem_id
        page = self.comms.open_problem_page()
        self.test_cases = self.parser.get_test_cases(page)
        print "Test cases fetching successful."

    def write_test_cases_to_file(self):
        print "Saving test cases..."
        folder_name = self.contest_id + self.problem_id + "_testcases/"

        #check if directory already exists
        proc = Popen(['find', folder_name], shell = False, stdout = PIPE)
        if proc.communicate()[0] != folder_name[:-1]:
            Popen(['mkdir', folder_name], shell = False, stdout = PIPE, stderr = PIPE)

        for case, i in zip(self.test_cases, range(0, len(self.test_cases))):
            f = open(folder_name + str(i) + ".in", "w+")
            f.write(case[0])
            f.close()
            f = open(folder_name + str(i) + ".out", "w+")
            f.write(case[1])
            f.close()
        print "Test cases saved."
        print DIVIDER

    def run(self):
        self.__compile()
        self.__fetch_test_cases()
        self.__write_test_cases_to_file()
        self.__run_all_test_cases()
