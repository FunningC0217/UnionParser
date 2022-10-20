from abc import ABCMeta, abstractmethod
from until.globallog import log
import os


class Parser:
    __metaclass = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def doParse(self, storage, files, file):
        log(__name__).critical('doParser ' + 'language:\"' + ','.join(self.language()) + '\", ' +
                               'file:\"' + file + '\"' +
                               'storage:\"' + storage + '\"')

    @abstractmethod
    def language(self):
        return []

    @abstractmethod
    def mimetypes(self):
        return []

    @abstractmethod
    def rootName(self):
        return ''
