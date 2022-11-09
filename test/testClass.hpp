#include <iostream>

union un1
{
    int intNum;
};

int gint = 10;

namespace na1
{
    namespace na2
    {
        static int testNNInt;
    }
}

struct AAA{
    int number;
    char ch;
    void AAAmethod();
};

class BBB : AAA
{
    AAA inC_aaa;
    int inC_number;
    char inC_ch;
public:
    BBB();
    virtual ~BBB();
    void BBBmethod();
};
