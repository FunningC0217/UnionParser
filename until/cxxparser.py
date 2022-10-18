from until.parser import Parser

class CxxParser(Parser):
    def doPaser(self, storage, file):
        pass

    def language(self):
        return ['C', 'C++']

    def mimetypes(self):
        return ['text/x-csrc', 'text/x-chdr', 'text/x-c++src', 'text/x-c++hdr']

    def rootName(self):
        return 'Cxx'