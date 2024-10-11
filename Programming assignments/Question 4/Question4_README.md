Introduction

My task is to apply slicing in Python and C-like language and show the results in the graphical image.

Steps:
- At first I created C++ matrix slicng with the corresponding header file. In order to view the source code, go to `SlicingMatrixOperation/SlicingMatrixOperation'. There is matrixSlicing.cpp. The code is written there alongside matrixSlicing.h .

- In order to create unit test, we need to somehow use c++ code in python. I created `.dll` in order to export functionality so other programs can use (including python). This solution file `.sln` is dedicated to create `.dll`.
In order to run this solution, Open Visual studio 2019, and build it. It will be created under x64.

-- C++ Code explanation:
It accepts 5 parameters, 1 pointers and 4 are normal integers.

~First is image (Denoting image matrix with 3 channeled)
~Second and third it is where slice start in height and end respectively

~Fourth and fifth it is where slice start in width and end respectively

In the code, if the slice difference either in height or width is 0, then the result will be `nullptr`.

If not, then the process will go in O(n^3). The process goes in the way article follows:
[Link Text](https://www.geeksforgeeks.org/auto-cropping-based-on-labeling-the-connected-components-using-matlab/)

After creating `.dll`, It is need to be called in python, so the environment is created. The file is located in `SlicingMatrixOperation/x64/Release/main.py` path.

UnitTest Environment is created. In `setUp` function, the dll is opened and function input output values are given.

Every test results will be saved in the directory you opened the `.exe` file with corresponding images. (I will come to this later)

HERE, THIS IS IMPORTANT !
Python here acts as validator, unit test creater and C++ acts as test taker, so python tests if C++ code can run the process correctly or not.

For validation part, I used `opencv` and `numpy` because it is known that their functionality works, so it is perfect it to act as validator for my C++ code.

How process goes:

At first, you have to have `Photos` directory alongside the `.exe` file to get it as input. In `Photos` directory, it can consists of multiple image files.

The test cases are generated dynamically so that we can check if the code works for dynamic (changing cases).

Slice start and end points with corresponding to the size of image are created and send to C++ alonside image matrix and get the results.

Then, the cropped image which C++ provided goes under the preprocess where it is applied `cv2.rectangle` to draw bouding boxes around it. 

Alongside this process, python preprocesser does the same thing logically as the C++ does including bounding box drawing.

Then, the cropped part will be merged with the original image in both programming languages and saved at the directory '.exe` runs with the name of `TestedCroppedImages`.

In each image, 5 different random types of transformations applied and in each transformation, the output images are shown , both with cropped ones and merged ones.

REQUIREMENTS:
This code is only accessable and usable in WINDOWS environment !!!
.Exe file is created for you to check how this program works so to not install some dependencies.

TestedCroppedImages folders will be created in the same directory as the `.exe` file stands.
In order to use this .exe, open terminal and write `./main.exe`. This is the case for to show the outputs. If you double click, it won't stay in the windows.

`.exe` file link:
[Link Text](https://drive.google.com/file/d/1tDfdHbQKl-rR0SiaYAaTHekIl0I0rDuY/view?usp=sharing)


In zip file, for the test reason, I added folder with images. You have to use that folder alongside the `.exe` file or it won't the input folder.