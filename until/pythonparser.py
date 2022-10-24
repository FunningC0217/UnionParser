from until.parser import Parser
from until.globallog import log
import parser

class PythonParser(Parser):

    def __init__(self):
        super(PythonParser, self).__init__()
    def load_suite(self, source_string):
        st = parser.suite(source_string)
        return st, st.compile()

    def load_expression(self, source_string):
        st = parser.expr(source_string)
        return st, st.compile()

    def doParse(self, storage, files, file):
        super(PythonParser, self).doParse(storage, files, file)
        f = open(file, 'r', encoding='utf8')
        print(self.load_suite(f.read()))

    def language(self):
        return ['Python']

    def mimetypes(self):
        return ['text/x-python']

    def rootName(self):
        return 'Python'
