#include "pch.h"

#include "matrixSlicing.h"

int*** MatrixSlicing(int*** image, int rowSliceStart, int rowSliceEnd,
					 int columnSliceStart, int columnSliceEnd) {

	if (rowSliceEnd - rowSliceStart == 0 || columnSliceEnd - columnSliceStart == 0)
		return nullptr;
	
	int*** slicedImage = new int** [rowSliceEnd - rowSliceStart];

	for (int i = 0; i < rowSliceEnd - rowSliceStart; i++) {
		slicedImage[i] = new int* [columnSliceEnd - columnSliceStart];
		
		for (int j = 0; j < columnSliceEnd - columnSliceStart; j++)
			slicedImage[i][j] = new int[3];
	}

	for (int i = 0; i < rowSliceEnd - rowSliceStart; i++) {
		for (int j = 0; j < columnSliceEnd - columnSliceStart; j++) {
			for (int k = 0; k < 3; k++)
				slicedImage[i][j][k] = image[rowSliceStart + i][columnSliceStart + j][k];
		}
	}

	return slicedImage;
}