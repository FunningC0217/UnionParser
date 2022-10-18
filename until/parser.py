from abc import ABCMeta, abstractmethod
import logging
import os

log = logging.getLogger(__name__)

class Parser:
    __metaclass = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def doParse(self, storage, file):
        log.critical('doParser ' + 'language:\"' + ','.join(self.language()) + '\", ' +
                     'file:\"' + file + '\", ' +
                     'storage:\"' + storage + os.sep + self.rootName() + '\"')

    @abstractmethod
    def language(self):
        return []

    @abstractmethod
    def mimetypes(self):
        return []

    @abstractmethod
    def rootName(self):
        return ''
