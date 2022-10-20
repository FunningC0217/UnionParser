#include "testClass.hpp"

void AAA::AAAmethod(){}

void BBB::BBBmethod(){}

BBB::~BBB(){
    AAA aaa;
}

BBB::BBB(){}

class CCC
{
    AAA aaa;
};