
from abc import ABCMeta, abstractmethod

class AstProgram:
    __metaclass = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def program(self):
        pass

    def language(self):
        pass

    def arguments(self, file):
        pass

class AstCxx(AstProgram):
    def program(self):
        return "clangd"
    def language(self):
        return "c/c++"
    def arguments(self, file):
        return ""

class ParserProxy:
    __astProgram = []
    def __init__(self):
        pass

    def regAstProgram(self, astProgram):
       if isinstance(astProgram, astProgram):
           self.__astProgram.insert(astProgram)
       else
           log