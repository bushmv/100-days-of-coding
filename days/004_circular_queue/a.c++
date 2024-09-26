#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{ 
    unsigned const int capacity = 4;
    unsigned int size = 0;
    int buffer[capacity];
    cout << sizeof(buffer) << endl;
    for (size_t i = 0; i < 100; i++)
    {
        buffer[size % capacity] = i;
        size ++;
    }
    for (const auto& e: buffer) {
        cout << e << " ";
    }
    
    return 0;
}
