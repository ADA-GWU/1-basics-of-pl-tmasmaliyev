from ctypes import CDLL
from ctypes import POINTER, c_int

import os, sys

import numpy as np
import unittest


class TestMatrixMultiply(unittest.TestCase):
    def setUp(self):
        self.dllPath = os.path.join(
            os.path.dirname(__file__),
            'MatrixMultiplication.dll'
        )

        # Since the code is only available for .exe, I can use sys.executable beacuse It is in `frozenMode`
        self.notepadCreatedDir = os.path.dirname(sys.executable)

        self.sourceDLL = CDLL(self.dllPath)

        self.sourceDLL.MatrixMultiplication.argtypes = [
            # region First Matrix Paremeters
            POINTER(POINTER(c_int)),
            c_int,
            c_int, 
            #endregion

            #region Second Matrix Paremeters
            POINTER(POINTER(c_int)),
            c_int,
            c_int, 
            #endregion
        ]

        self.sourceDLL.MatrixMultiplication.restype = POINTER(POINTER(c_int))
    
    def test_multiply_compatible_shapes(self):

        with open(
                    os.path.join(
                        self.notepadCreatedDir, 
                        'test_multiply_compatible_shapes.txt'
                    ),
                    'w'
            ) as f:

            for testNumber in range(1, 10):
                f.write(f'Test Number : {testNumber}\n\n')

                n = np.random.randint(1,  8) # In both matrices, it will be the same.
                m = np.random.randint(1, 11) # First matrix Row size
                k = np.random.randint(1, 11) # second matrix Column size

                #region First Matrix Shape  (M, N)
                leftMatrix = np.random.randint(low=0, high=20, size=(m, n))

                leftMatrixPreProcessed = (POINTER(c_int) * m) ()
                
                for j in range(m):
                    leftMatrixPreProcessed[j] = (c_int * n) (*leftMatrix[j])

                f.write(f'Left Matrix with shape : ({m}, {n}) \n\n')
                
                text = str(leftMatrix)
                textPreprocessed = text.replace('[', ' ').replace(']', ' ')

                f.write(textPreprocessed + '\n\n')
                #endregion

                #region Second Matrix Shape (N, K)
                rightMatrix = np.random.randint(low = 0, high=20, size=(n, k))

                rightMatrixPreProcessed = (POINTER(c_int) * n) ()

                for j in range(n):
                    rightMatrixPreProcessed[j] = (c_int * k) (*rightMatrix[j])
                
                f.write(f'Right Matrix with shape : ({n}, {k}) \n\n')

                text = str(rightMatrix)
                textPreprocessed = text.replace('[', ' ').replace(']', ' ')

                f.write(textPreprocessed + '\n\n')

                #endregion

                resultMatrix = leftMatrix @ rightMatrix # This line is for assertion to test if multiplication in C++ code true or not.

                f.write(f'Expected Matrix with shape ({m}, {k})\n\n')

                text = str(resultMatrix)
                textPreprocessed = text.replace('[', ' ').replace(']', ' ')

                f.write(textPreprocessed + '\n\n')

                # C++ Call for MatrixMultiplication
                outMatrix = self.sourceDLL.MatrixMultiplication(
                    leftMatrixPreProcessed,  m, n,
                    rightMatrixPreProcessed, n, k
                )

                f.write(f'Output Matrix \n\n')

                # If the result provides NULLPTR, then it is incorrect !
                if not outMatrix:
                    f.write('NULLPTR\n\n')

                    raise AssertionError(f"Failed : Test Number : {testNumber}. Check Out the notepad to get matrices !")

                outMatrixPreProcessed = np.zeros(dtype=np.int32, shape=(m, k))

                for i in range(m):
                    for j in range(k):
                        outMatrixPreProcessed[i][j] = outMatrix[i][j]
                    
                text = str(outMatrixPreProcessed)
                textPreprocessed = text.replace('[', ' ').replace(']', ' ')

                f.write(textPreprocessed + '\n\n')


                # Test if they are same or not. If not, then throw exception
                # If everything is true, then the shape must be (M, K)
                for i in range(m):
                    for j in range(k):
                        assert outMatrixPreProcessed[i][j] == resultMatrix[i][j], f"Failed : Test Number : {testNumber}. Check Out the notepad to get matrices !"

                f.write(f'Test Number : {testNumber}, successfully completed !\n\n')
        
    def test_multiply_incompatible_shapes(self):
        
        with open(
                    os.path.join(
                        self.notepadCreatedDir, 
                        'test_multiply_incompatible_shapes.txt'
                    ),
                    'w'
            ) as f:

            for testNumber in range(1, 10):
                f.write(f'Test Number : {testNumber}\n\n')

                n = np.random.randint(1,  8) # It will not be the same.
                m = np.random.randint(1, 11) # First matrix Row size

                tValues = np.arange(1, 8)
                tValues = tValues[tValues != n]

                t = int(np.random.choice(tValues, 1)[0]) # Seond matrix Row size
                k = np.random.randint(1, 11) # second matrix Column size

                #region First Matrix Shape  (M, N)
                leftMatrix = np.random.randint(low=0, high=20, size=(m, n))

                leftMatrixPreProcessed = (POINTER(c_int) * m) ()
                
                for j in range(m):
                    leftMatrixPreProcessed[j] = (c_int * n) (*leftMatrix[j])

                f.write(f'Left Matrix with shape : ({m}, {n}) \n\n')
                
                text = str(leftMatrix)
                textPreprocessed = text.replace('[', ' ').replace(']', ' ')

                f.write(textPreprocessed + '\n\n')
                #endregion

                #region Second Matrix Shape (T, K)
                rightMatrix = np.random.randint(low = 0, high=20, size=(t, k))

                rightMatrixPreProcessed = (POINTER(c_int) * t) ()

                for j in range(t):
                    rightMatrixPreProcessed[j] = (c_int * k) (*rightMatrix[j])
                
                f.write(f'Right Matrix with shape : ({t}, {k}) \n\n')

                text = str(rightMatrix)
                textPreprocessed = text.replace('[', ' ').replace(']', ' ')

                f.write(textPreprocessed + '\n\n')

                #endregion

                f.write(f'Expected Matrix \n\n')

                f.write("It is not possible !" + '\n\n')

                # C++ Call for MatrixMultiplication
                outMatrix = self.sourceDLL.MatrixMultiplication(
                    leftMatrixPreProcessed,  m, n,
                    rightMatrixPreProcessed, t, k
                )

                f.write(f'Output Matrix \n\n')

                # If the result provides NULLPTR, then it is incorrect !
                if not outMatrix:
                    f.write('It is not possible !\n\n')
                else:
                    raise AssertionError(f"Failed : Test Number : {testNumber}. Check Out the notepad to get matrices !")

                f.write(f'Test Number : {testNumber}, successfully completed !\n\n')

        
if __name__ == '__main__':
    unittest.main()