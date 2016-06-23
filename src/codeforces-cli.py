from CodeforcesCLI import CodeforcesCLI
import sys

def main():
    if(len(sys.argv) < 2):
        print "Usage: "
        print "\tcodeforces-cli filename [language] [compiler]\n"
        print "\t[language] can take the following values: "
        print "\t\tc++"

        return 0
    else:
        obj = CodeforcesCLI(sys.argv[1])
        obj.run()

        return 1
if __name__ == "__main__":
    main()
