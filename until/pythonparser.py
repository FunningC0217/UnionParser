from until.parser import Parser

class PythonParser(Parser):
    def doPaser(self, storage, file):
        pass

    def language(self):
        return ['Python']

    def mimetypes(self):
        return ['text/x-python']

    def rootName(self):
        return 'Python'
