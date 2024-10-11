#include "pch.h"

#include "matrixMultiply.h"

int** MatrixMultiplication(int** leftMatrix,  int leftMatrixRowLength,  int leftMatrixColumnLength,
					       int** rightMatrix, int rightMatrixRowLength, int rightMatrixColumnLength) {
	
	if (leftMatrixColumnLength != rightMatrixRowLength) {
		return nullptr;
	}

	int** resultMatrix = new int* [leftMatrixRowLength];

	for (int i = 0; i < leftMatrixRowLength; i++)
		resultMatrix[i] = new int[rightMatrixColumnLength];

	for (int i = 0; i < leftMatrixRowLength; i++) {
		for (int j = 0; j < rightMatrixColumnLength; j++) {
			resultMatrix[i][j] = 0;

			for (int k = 0; k < leftMatrixColumnLength; k++) {
				resultMatrix[i][j] += leftMatrix[i][k] * rightMatrix[k][j];
			}
		}
	}

	return resultMatrix;
}