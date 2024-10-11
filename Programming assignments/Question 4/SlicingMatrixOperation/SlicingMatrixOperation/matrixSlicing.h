
#ifndef MATRIXSLICING_H
#define MATRIXSLICING_H

#include <stdio.h>

#define EXPORTABLE_API __declspec(dllexport)

extern "C" {
	EXPORTABLE_API int*** MatrixSlicing(int*** image, int rowSliceStart, int rowSliceEnd,
								 		int columnSliceStart, int columnSliceEnd);

}
#endif