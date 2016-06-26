#!/usr/bin/python

from CodeforcesCLI import CodeforcesCLI
import sys


def print_usage():
    print "Usage: "
    print "\tcodeforces-cli [test | submit] path-to-file [-c compiler]"
    print "\nNOTE: Filename must be of the following format 'contestIDproblemID', Example: 608a.cpp, 604b.cpp, 607a.py"
    print "      Performs tests if not mentioned by default."
    print "Options and arguments: "
    print "test         : Execute your program against test cases fetched from codeforces"
    print "submit       : Submits your program to codeforces"
    print "path-to-file : Path to your source file"
    print "-c compiler  : Specify compiler to use. 'compiler' must be replaced with the compiler command you use, Example: g++, c++, javac, etc"


def main():

    if len(sys.argv) < 2:
        print_usage()
        return 1

    compiler = "g++"
    file_location = None
    action = "test"

    if sys.argv[1] != "test" and sys.argv[1] != "submit":
        file_location = sys.argv[1]
    else:
        file_location = sys.argv[2]

    if "-c" in sys.argv:
        index = sys.argv.index("-c")
        if(index + 1 < len(sys.argv)):
            compiler = sys.argv[index + 1]
        else:
            print_usage()
            return 1

    if(action == "test"):
        obj = CodeforcesCLI(file_location, compiler)
        obj.run()

        return 0

if __name__ == "__main__":
    main()
