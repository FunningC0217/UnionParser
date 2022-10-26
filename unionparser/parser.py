from abc import ABCMeta, abstractmethod
from unionparser.globallog import log
from unionparser.syntaxtree import SyntaxTreeNode, findParent
import os

class Parser:
    __metaclass = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def doParse(self, storage, files, file):
        log(__name__).critical('doParser ' + 'language:\"' + ','.join(self.language()) + '\", ' +
                               'file:\"' + file + '\", ' +
                               'storage:\"' + storage + '\"')

    @abstractmethod
    def astTreeFromOut(self, ast_dump_out: str) -> SyntaxTreeNode:
        return None

    @abstractmethod
    def language(self):
        return []

    @abstractmethod
    def mimetypes(self):
        return []

    @abstractmethod
    def rootName(self):
        return ''

    @staticmethod
    def reference():
        return '.reference'

    @staticmethod
    def declared():
        return '.declared'

    @staticmethod
    def definitions():
        return '.definitions'

    @staticmethod
    def record():
        return '.record'

    @staticmethod
    def fileHasLine(file, line):
        has_line = False
        if os.path.exists(file):
            f = open(file, mode="r", encoding="utf8")
            r_line = f.readline()
            while r_line:
                if line == r_line:
                    has_line = True
                    break
                r_line = f.readline()
            f.close()
        return has_line

