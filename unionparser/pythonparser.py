from abc import ABC

from unionparser.parser import Parser
from unionparser.globallog import log
import parser
import ast
import os
from syntaxtree import SyntaxTreeNode, findParent


class PyAstCvt(ast.NodeVisitor):
    def __init__(self, filePath: str):
        super(PyAstCvt, self).__init__()
        self.__stack = 0
        self.root = SyntaxTreeNode()
        self.root.child = []
        self.root.prefix_len = self.__stack
        self.root.src_file_path = filePath
        f = open(filePath, 'r', encoding='utf8')
        src = f.read()
        f.close()
        module_tree = ast.parse(src)
        self.visit(module_tree)

    @staticmethod
    def getClassDefString(node: ast.ClassDef):
        return "class " + PyAstCvt.getClassDefName(node)

    @staticmethod
    def getClassDefName(node: ast.ClassDef):
        return getattr(node, "name")

    @staticmethod
    def getFuncDefArgsString(node: ast.arguments):
        ret = ""
        for arg in getattr(node, "args"):
            if ret != "":
                ret += ","
            ret += arg.arg
        return ret

    @staticmethod
    def getFuncDefDecoratorListString(node: ast.FunctionDef):
        ids = ""
        dec_list = getattr(node, "decorator_list")
        for idx in range(0, len(dec_list)):
            if idx != 0:
                ids += ","
            else:
                ids += getattr(dec_list[idx], "id")
        return ids

    @staticmethod
    def getFuncDefRange(node: ast.FunctionDef) -> []:
        return [str(getattr(node, "lineno")), str(getattr(node, "col_offset"))]

    @staticmethod
    def getClassDefRange(node: ast.ClassDef) -> []:
        return [str(getattr(node, "lineno")), str(getattr(node, "col_offset"))]

    @staticmethod
    def getFuncDefString(node: ast.FunctionDef):
        ret = ""
        if not isinstance(node, ast.FunctionDef):
            return ret
        else:
            dec_list = PyAstCvt.getFuncDefDecoratorListString(node)
            print(dec_list)
            arguments = getattr(node, "args")
            ret += getattr(node, "name")
            ret += "(" + PyAstCvt.getFuncDefArgsString(arguments) + ")"
        return ret

    @staticmethod
    def getImportString(node):
        if not isinstance(node, ast.Import):
            return ""
        else:
            return ""

    @staticmethod
    def defNodeFilter():
        return [ast.ClassDef.__name__, ast.FunctionDef.__name__]

    def visit(self, node):
        if isinstance(node, ast.AST):
            print(self.__stack, self.__stack * "    ", node.__class__.__name__)
        for field in node._fields:
            val = getattr(node, field)
            if isinstance(val, list):
                self.__stack += 1
                print(self.__stack, self.__stack * "    ", field, "=", val)
                for one in val:
                    self.visit(one)
                self.__stack -= 1
            elif isinstance(val, ast.AST):
                self.__stack += 1
                print(self.__stack, self.__stack * "    ", field, "=", val)
                self.visit(val)
                self.__stack -= 1
            else:
                print(self.__stack, self.__stack * "    ", field, "=", val)
                
        # if not isinstance(node, ast.Module):
        #     print('n', self.__stack * "    ", node.__class__.__name__)
        #     new_node = SyntaxTreeNode()
        #     new_node.child = []
        #     new_node.prefix_len = self.__stack
        #     new_node.type = node.__class__.__name__
        #     parent = findParent(self.root, self.__stack)
        #     new_node.parent = parent
        #     parent.child.append(new_node)
        # 
        #     for field in node._fields:
        #         field_node = SyntaxTreeNode()
        #         field_node.child = []
        #         field_node.prefix_len = self.__stack
        #         field_node.type = field
        #         val = getattr(node, field)
        #         if isinstance(val, list):
        #             self.__stack += 1
        #             for one in val:
        #                 print("b", self.__stack * "    ", one.__class__.__name__)
        #                 super(PyAstCvt, self).visit(one)
        #             self.__stack -= 1
        #         elif isinstance(val, ast.AST):
        #             self.__stack += 1
        #             super(PyAstCvt, self).visit(val)
        #             self.__stack -= 1
        #         else:
        #             print("f", self.__stack * "    ", field, "=", repr(val))
        #         field_node.parent = new_node
        #         new_node.child.append(field_node)
        # else:
        #     self.root.type = ast.Module.__class__.__name__
        # 
        # self.__stack += 1
        # super(PyAstCvt, self).visit(node)
        # self.__stack -= 1


class PythonParser(Parser, ABC):
    def __init__(self):
        super(PythonParser, self).__init__()

    def getSyntaxTree(self, file: str):
        cvt = PyAstCvt(file)
        return cvt.root

    def doParse(self, storage, files, file):
        super(PythonParser, self).doParse(storage, files, file)
        ast_root = self.getSyntaxTree(file)
        print(ast_root)

    def language(self):
        return ['Python']

    def mimetypes(self):
        return ['text/x-python']

    def rootName(self):
        return 'Python'
