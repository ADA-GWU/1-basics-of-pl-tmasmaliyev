
#ifndef MULTIPLY_H
#define MULTIPLY_H

#define EXPORTABLE_API __declspec(dllexport)

#include <stdio.h>

extern "C" {
	EXPORTABLE_API int** MatrixMultiplication(int** leftMatrix,  int leftMatrixRowLength,  int leftMatrixColumnLength,
											  int** rightMatrix, int rightMatrixRowLength, int rightMatrixColumnLength);
}

#endif