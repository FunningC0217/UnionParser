import os


def globalFunc():
    pass

class Test:
    def __init__(self, va1):
        self.member = ""
        self.list = ""
        self.__member = ""
        self.__list = ""

    @staticmethod
    def sta_method(self, va2) -> int:
        sm_a = 10
        return sm_a

    def method(self, va1, va2, va3):
        m_a = 20
        return m_a

    def __pri_method(self, va1, va2, va3):
        pm_a = 10
        return pm_a

    
class Test1:
    def __init__(self) -> None:
        pass

    def test1(self):
        pass

class Test2(Test1):
    pass


if __name__ == '__main__':
    print('HelloWorld')
