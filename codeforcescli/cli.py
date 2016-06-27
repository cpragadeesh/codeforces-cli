from CodeforcesCLI import CodeforcesCLI
import sys


def print_usage():
    print "Usage: "
    print "\tcfcli [-h] [test | submit] path-to-file [-c compiler]"
    print "\nNOTE: Filename must be of the following format 'contestIDproblemID', Example: 608a.cpp, 604b.cpp, 607a.py"
    print "      Performs tests if not mentioned by default."
    print "Options and arguments: "
    print "-h           : Prints this message"
    print "test         : Execute your program against test cases fetched from codeforces"
    print "submit       : Submits your program to codeforces"
    print "path-to-file : Path to your source file"
    print "-c compiler  : Specify compiler to use. 'compiler' must be replaced with the compiler command you use, Example: g++, c++, javac, etc"


def main():

    if len(sys.argv) <= 3:
        print_usage()
        return 1

    action = sys.argv[1]
    compiler = sys.argv[2]
    file_location = sys.argv[3]
    compiler_options = ""
    if len(sys.argv) >= 4:
        compiler_options = ' '.join(sys.argv[4: ])

    if action == '-h':
        print_usage()
        return 0

    if action == "-t":
        obj = CodeforcesCLI(compiler, file_location, compiler_options)
        obj.run()

        return 0

if __name__ == "__main__":
    main()
