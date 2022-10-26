from logging import root

from unionparser.parser import Parser
from unionparser.globallog import log
from unionparser.syntaxtree import SyntaxTreeNode, findParent
import os

class JavaParser(Parser):
    def __init__(self):
        super(JavaParser, self).__init__()

    def astTreeFromOut(self, ast_dump_out: str):
        e_tree = None
        lines = ast_dump_out.split("\n")
        for line in lines:
            if line != "":
                line = line.replace("\n", "")
                elms = line.split(" -> ")
                str_range = elms[1].split(" ")
                e_type = elms[0]
                e_string = str_range[0]
                e_range = str_range[1]
                e_types = e_type.replace("|--", "   ").replace("`--", "   ").replace("|", " ").split(" ")
                e_type = e_types[len(e_types) - 1]
                if len(e_types) == 1:
                    e_tree = SyntaxTreeNode
                    e_tree.range = e_range
                    e_tree.type = e_type
                    e_tree.string = e_string
                else:
                    prefix_len = len(e_types[0:len(e_types) - 1])
                    parent = findParent(e_tree, prefix_len)
                    if parent:
                        node = SyntaxTreeNode()
                        node.prefix_len = prefix_len
                        node.type = e_type
                        node.range = e_range
                        node.parent = parent
                        node.string = e_string
                        node.child = []
                        log(__name__).critical("find parent: " + parent.string + " add child: " + e_string)
                        parent.child.append(node)
        return e_tree

    def doParse(self, storage, files, file):
        super(JavaParser, self).doParse(storage, files, file)
        p = os.popen("java -jar "
                     + os.path.abspath(os.path.dirname(__file__))
                     + os.path.sep + "3rd/checkstyle-10.3.4-all.jar -t "
                     + file)
        ast_tree = self.astTreeFromOut(p.read())

    def language(self):
        return ['Java']

    def mimetypes(self):
        return ['text/x-java']

    def rootName(self):
        return 'Java'
