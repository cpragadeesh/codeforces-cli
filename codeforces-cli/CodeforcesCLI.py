import sys
from subprocess import Popen, PIPE, call
from CodeforcesComms import CodeforcesComms
from Parser import Parser

DIVIDER = "----------------------------------------------------"

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

    def _config_comms(self, username = None, password = None):
        self.comms.contest_id = str(self.contest_id)
        self.comms.problem_id = str(self.problem_id)
        self.comms.username = username
        self.comms.password = password

    def _parse_file_name(self):

        contest_id_end = self.file_name.find(".")
        contest_id_end = contest_id_end - 1

        self.contest_id = self.file_name[ :contest_id_end]
        self.problem_id = self.file_name[contest_id_end: contest_id_end + 1]

        self._config_comms()

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
        page = self.comms.open_problem_page()
        self.test_cases = self.parser.get_test_cases(page)
        folder_name = self.contest_id + self.problem_id + "_testcases/"

        #check if directory already exists
        proc = Popen("ls | grep " + folder_name)
        Popen(['mkdir', folder_name])

        for case, i in zip(self.test_cases, range(0, len(test_cases))):
            f = open(folder + str(i), "w+")
            f.write(case)
            f.close()

    def run(self):
        self.compile()
        self._parse_file_name()

        if self.fetch_test_cases():
            self.run_all_test_cases()
