from unionparser.parser import Parser
from unionparser.globallog import log
import parser
import ast

class PythonParser(Parser):
    def __init__(self):
        super(PythonParser, self).__init__()

    def doParse(self, storage, files, file):
        super(PythonParser, self).doParse(storage, files, file)
        f = open(file, 'r', encoding='utf8')
        src = f.read()
        print(ast.dump(ast.parse(src)))

    def language(self):
        return ['Python']

    def mimetypes(self):
        return ['text/x-python']

    def rootName(self):
        return 'Python'
