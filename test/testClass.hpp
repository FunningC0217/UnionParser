#include <iostream>

union un1
{
    int intNum;
};

namespace na1
{
    namespace na2
    {

    }
}

struct AAA{
    int number;
    char ch;
    void AAAmethod();
};

class BBB
{
    AAA inC_aaa;
    int inC_number;
    char inC_ch;
public:
    BBB();
    virtual ~BBB();
    void BBBmethod();
};
