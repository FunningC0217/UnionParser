from until.parser import Parser
from until.globallog import log
import javac_parser

class JavaParser(Parser):
    def __init__(self):
        super(JavaParser, self).__init__()
        self.__java_parser = javac_parser.Java()

    def doParse(self, storage, files, file):
        super(JavaParser, self).doParse(storage, files, file)
        f = open(file, 'r', encoding='utf8')
        res = self.__java_parser.lex(f.read())
        print(res)

    def language(self):
        return ['Java']

    def mimetypes(self):
        return ['text/x-java']

    def rootName(self):
        return 'Java'
