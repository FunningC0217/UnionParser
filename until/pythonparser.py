from until.parser import Parser
from until.globallog import log

class PythonParser(Parser):

    def __init__(self):
        super(PythonParser, self).__init__()

    def doParse(self, storage, files, file):
        super(PythonParser, self).doParse(storage, files, file)

    def language(self):
        return ['Python']

    def mimetypes(self):
        return ['text/x-python']

    def rootName(self):
        return 'Python'
