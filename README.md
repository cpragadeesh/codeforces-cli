#Codeforces Command Line Interface

##How to install:
* Download from the latest release from [here](https://github.com/cpragadeesh/codeforces-cli/releases).
* Unpack the file.
* Run the following command:

  `python setup.py install`

 *NOTE: You need to be root to do this. Switch to root or use sudo.*

##How to use:
1. Save your source file in the following format:<br>
    >ContestIDProblemID.extension


    *Examples: 608a.cpp, 608b.cpp, 604b.py, 602.java*<br>
    *NOTE: Contest ID is found in the URL of the problem. Contest ID is not same as Round Number.*

2. Testing your program:<br>
    Run the following command:

      `cfcli -t <compiler> <path-to-file> [<compiler_options>]`

   *Example:*

      `cfcli -t g++ ~/Codes/608a.cpp -std=c++14`


Get more usage info by using the -h option

    `cfcli -h`

<p align="center">
<img src="http://i67.tinypic.com/2liu3w9.jpg"/>
</p>
