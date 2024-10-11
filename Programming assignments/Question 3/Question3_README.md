Introduction

My task is to implement matrix multiplication in both Python and C-like languages (in this case, it will be C++).

Steps:
- At first, I created C++ matrix multiplication with the corresponding header file. In order to view the source code, go to `MatrixMultiplication/MatrixMultiplication'. There is matrixMultiply.cpp. The code is written there alongside matrixMultiply.h .

- In order to create unit test, we need to somehow use c++ code in python. I created `.dll` in order to export functionality so other programs can use (including python). This solution file `.sln` is dedicated to create `.dll`.
In order to run this solution, Open Visual studio 2019, and build it. It will be created under x64.

-- C++ Code explanation:
It accepts 6 parameters, 2 pointers and 4 are normal integers.

~First is leftMatrix (Denoting left multiplier matrix)
~Second and third its row and column lengths respectively

~Fourth is rightMatrix (Denoting right multiplied matrix)
~Fifth and sixth its row and column lengths respectively

In the code, if the first matrix column is not equal to second matrix row, then it will return `nullptr`

If not, then the process will go in O(n^3). The process goes in the way article follows:
[Link Text](https://en.wikipedia.org/wiki/Matrix_multiplication#:~:text=For%20matrix%20multiplication%2C%20the%20number,B%20is%20denoted%20as%20AB.)


After creating `.dll`, It is need to be called in python, so the environment is created. The file is located in `MatrixMultiplication/x64/Release/main.py` path.

UnitTest Environment is created. In `setUp` function, the dll is opened and function input output values are given.

There will be two tests :
- Test multiply compatible shapes
- Test multiply incompatible shapes

Every test results will be saved in the directory you opened the `.exe` file (I will come to this later)

HERE, THIS IS IMPORTANT !
Python here acts as validator, unit test creater and C++ acts as test taker, so python tests if C++ code can run the process correctly or not.

For validation part, I used `numpy` because it is known that their functionality works, so it is perfect it to act as validator for my C++ code.

How process goes:

Each test functions, notepad is created in order to see what is input and expected result and what c++ provided.

The test cases are generated dynamically so that we can check if the code works for dynamic (changing cases).

Matrices with corresponding sizes are created and send to C++ and get the results and tested with numpy calculated multiplication.

If the results are the same, then everything is okay, if not, then, the AssertionError is raised.

In test multiply incompatible case, It has to return nullptr, if not the something is wrong.

REQUIREMENTS:
This code is only accessable and usable in WINDOWS environment !!!
.Exe file is created for you to check how this program works so to not install some dependencies.


Notepad files will be created in the same directory as the `.exe` file stands.
In order to use this .exe, open terminal and write `./main.exe`. This is the case for to show the outputs. If you double click, it won't stay in the windows.

`.exe` file link:
[Link Text](https://drive.google.com/file/d/1pyb4bAeuFUFBXzLKQv901phVs3MOf347/view?usp=sharing)
