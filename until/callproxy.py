import mimetypes
import os
from until.parser import Parser

import logging
log = logging.getLogger(__name__)

class CallProxy:
    __parsers = []
    __storage = ''
    __language = ''
    __workspace = ''

    def __init__(self):
        pass

    def workspace(self):
        return self.__workspace

    def setWorkspace(self, workspace):
        self.__workspace = workspace

    def setStorage(self, storage):
        self.__storage = storage

    def storage(self):
        return self.__storage

    def setLanguage(self, language):
        self.__language = language

    def language(self):
        return self.__language

    def supportLanguages(self):
        languages = []
        for ins in self.__parsers:
            languages += ins.language()
        return languages

    def addParser(self, parser):
       if isinstance(parser, Parser):
           self.__parsers.append(parser)
       else:
           log.critical("Can't regiest handler for not Parser")

    def doParse(self):
        for root, dirs, files in os.walk(self.__workspace):
            for file in files:
                for parser in self.__parsers:
                    for mime in mimetypes.guess_type(root + os.sep + file):
                        if mime in parser.mimetypes():
                            parser.doParse(self.__storage, root + os.sep + file)

