from ctypes import CDLL
from ctypes import POINTER, c_int

import os, sys

import numpy as np
from copy import deepcopy
import cv2

import unittest


class TestMatrixSlicing(unittest.TestCase):
    def setUp(self):
        self.dllPath = os.path.join(
            os.path.dirname(__file__),
            'SlicingMatrixOperation.dll'
        )

        # Since the code is only available for .exe, I can use sys.executable beacuse It is in `frozenMode`
        self.curDir = os.path.dirname(sys.executable)
        self.imageDir = os.path.join(self.curDir, 'Photos')
        
        os.makedirs(os.path.join(self.curDir, 'TestedCroppedImages'))

        self.imageSaveDir = os.path.join(self.curDir, 'TestedCroppedImages')

        self.sourceDLL = CDLL(self.dllPath)

        self.sourceDLL.MatrixSlicing.argtypes = [
            POINTER(POINTER(POINTER(c_int))),
            c_int,
            c_int,
            c_int,
            c_int
        ]

        self.sourceDLL.MatrixSlicing.restype = POINTER(POINTER(POINTER(c_int)))
    
    def test_slicing(self):

        imageFiles = os.listdir(os.path.join(self.curDir, 'Photos'))

        for testNumber, imageFile in enumerate(imageFiles, 1):
            image = cv2.imread(os.path.join(self.curDir, 'Photos', imageFile))

            curTestedImageDir = os.path.join(self.curDir, 'TestedCroppedImages', f'Photo{testNumber}')
            os.makedirs(curTestedImageDir)
            
            imagePreprocessed = (POINTER(POINTER(c_int)) * image.shape[0]) ()

            for i in range(image.shape[0]):
                imagePreprocessed[i] = (POINTER(c_int) * image.shape[1]) ()

                for j in range(image.shape[1]):
                    imagePreprocessed[i][j] = (c_int * 3) (*image[i][j])

            for i in range(5):
                image1 = deepcopy(image)
                image2 = deepcopy(image)

                rowSliceStart = np.random.randint(low=0, high=image.shape[0])
                rowSliceEnd = np.random.randint(low=rowSliceStart + 1, high=image.shape[0])

                columnSliceStart = np.random.randint(low=0, high=image.shape[1])
                columnSliceEnd = np.random.randint(low=columnSliceStart + 1, high=image.shape[1])

                outMatrixSliced = self.sourceDLL.MatrixSlicing(
                    imagePreprocessed, 
                    rowSliceStart,    rowSliceEnd,
                    columnSliceStart, columnSliceEnd
                )

                imageCroppedResult = image1[rowSliceStart:rowSliceEnd, columnSliceStart:columnSliceEnd]

                outMatrixPreprocessed = np.zeros(
                    dtype=np.float32,
                    shape=(rowSliceEnd - rowSliceStart, columnSliceEnd - columnSliceStart, 3)
                )

                for j in range(rowSliceEnd - rowSliceStart):
                    for k in range(columnSliceEnd - columnSliceStart):
                        for t in range(3):
                            outMatrixPreprocessed[j][k][t] = outMatrixSliced[j][k][t]

                os.makedirs(os.path.join(curTestedImageDir, f'Transform {i + 1}'))

                cv2.imwrite(os.path.join(curTestedImageDir, f'Transform {i + 1}', 'CroppedByPython.jpg'), imageCroppedResult)
                cv2.imwrite(os.path.join(curTestedImageDir, f'Transform {i + 1}', 'CroppedByC++.jpg'), outMatrixPreprocessed)

                # Create red bounding box around cropped image to detect where it was cropped.
                # In this case, OPENCV are just using for ASSERTION !
                cv2.rectangle(imageCroppedResult, 
                              (1, 1), 
                              (imageCroppedResult.shape[1] - 1, imageCroppedResult.shape[0] - 1),
                              color=(0, 0, 255),
                              thickness=2
                ) 

                image1[rowSliceStart : rowSliceEnd, columnSliceStart : columnSliceEnd] = imageCroppedResult

                cv2.rectangle(outMatrixPreprocessed, 
                              (1, 1),
                              (outMatrixPreprocessed.shape[1] - 1, outMatrixPreprocessed.shape[0] - 1),
                              color=(0, 0, 255), 
                              thickness=2
                )

                image2[rowSliceStart : rowSliceEnd, columnSliceStart : columnSliceEnd] = outMatrixPreprocessed

                cv2.imwrite(os.path.join(curTestedImageDir, f'Transform {i + 1}', 'CroppedByPythonInAllImage.jpg'), image1)
                cv2.imwrite(os.path.join(curTestedImageDir, f'Transform {i + 1}', 'CroppedByC++InAllImage.jpg'), image2)   
        
if __name__ == '__main__':
    unittest.main()