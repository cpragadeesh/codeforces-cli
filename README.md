#Codeforces Command Line Interface

##How to install:
Run the following command:

  `python setup.py install`

 *NOTE: You need to be root to do this. Switch to root or use sudo.*

##How to use:
1. Save your source file in the following format:

    >ContestIDProblemID.extension

    *Examples: 608a.cpp, 608b.cpp, 604b.py, 602.java*


    *NOTE: Contest ID is found in the URL of the problem. Contest ID is not same as Round Number.*

2. To test you program:

    Run the following command:

      `cfcli test <path-to-file>`

   *Example:*

      `cfcli test Documents/Codes/608a.cpp`

    You can choose your compiler by using -c tag. For example, If you compile your program using the following command:

      `g++ 608a.cpp`

    Then set the compiler by appending the "-c g++"

      `cfcli test 608a.cpp -c g++`

Get more usage info by using the -h tag

    `cfcli -h`

<p align="center">
<img src="http://i67.tinypic.com/2liu3w9.jpg"/>
</p>
