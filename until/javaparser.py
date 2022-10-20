from until.parser import Parser
from until.globallog import log

class JavaParser(Parser):
    def __init__(self):
        super(JavaParser, self).__init__()

    def doParse(self, storage, files, file):
        super(JavaParser, self).doParse(storage, files, file)

    def language(self):
        return ['Java']

    def mimetypes(self):
        return ['text/x-java']

    def rootName(self):
        return 'Java'
