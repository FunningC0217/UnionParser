#include <iostream>

using namespace std;
struct ABC{
};

struct CCC{
};

int main()
{
    std::cout << "Hello World!" << std::endl;    
    ABC *p = new ABC();
    delete p; delete p;
    return 0;
}
