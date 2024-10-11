#include <iostream>
#include <vector>

int main() {
    int array[3] = {1, 2, 3};

    std::vector<int> vec = {1, 2, 3};

    std::cout << "Size of the array : " << sizeof(array) << " bytes" << std::endl;

    std::cout << "Size of the vector : " << sizeof(vec) << " bytes" << std::endl; 
}