from CodeforcesCLI import CodeforcesCLI
import sys

def print_usage():
    print "Usage: "
    print "\tcodeforces-cli action file [compiler]\n"

    print "\t[action] takes the following values: "
    print "\t\ttest -- Compiles and runs your program against test cases fetched from codeforces"

    print "\n\t[compiler] defaults to g++\n"

def main():

    if(len(sys.argv) < 3):
        print_usage()
        return 1

    else:

        compiler = "g++"
        file_location = sys.argv[2]
        action = sys.argv[1]

        if(action == "test"):
            if(len(sys.argv) >= 4):
                compiler = sys.argv[3]


            obj = CodeforcesCLI(file_location, compiler)
            obj.run()

        else:
            print_usage()

        return 0

if __name__ == "__main__":
    main()
