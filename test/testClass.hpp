#include <iostream>
// template<class T, unsigned Min>

// class small_vector
// {
//         small_vector()
//         {
//         }

//         small_vector(const small_vector<T, Min> &o)
//         {
//             *this = o;
//         }
// };

typedef union {
    typedef struct {
        double dob;
    } Struct;
}Un;



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
