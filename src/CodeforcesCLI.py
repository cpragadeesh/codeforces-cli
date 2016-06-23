import sys
from subprocess import Popen, PIPE

DIVIDER = "----------------------------------------------------"

class CodeforcesCLI():

    def __init__(self, file_name, lang = "c++", compiler = "c++"):
        self.file_name = file_name
        self.lang = lang
        self.compiler = compiler

    def compile(self):

        print DIVIDER
        print "Compiling " + self.file_name + " using " + self.compiler
        compilation = Popen([self.compiler, self.file_name])
        compilation_output = compilation.communicate()

        if compilation.returncode == 0:
            print "Compilation successful!"

        print DIVIDER

        return compilation.returncode

    def run_all_cases(self):
        pass

    def fetch_cases(self):
        pass

    def run(self):
        self.compile()
