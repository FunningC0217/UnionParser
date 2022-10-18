from until.parser import Parser

class JavaParser(Parser):
    def doParse(self, storage, file):
        pass

    def language(self):
        return ['Java']

    def mimetypes(self):
        return ['text/x-java']

    def rootName(self):
        return 'Java'
