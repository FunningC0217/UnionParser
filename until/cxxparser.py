from until.parser import Parser
from until.globallog import log

import mimetypes
import clang.cindex
from clang.cindex import Index  # 主要API
from clang.cindex import Config  # 配置
from clang.cindex import SourceLocation
from clang.cindex import CursorKind  # 索引结点的类别
from clang.cindex import TypeKind  # 节点的语义类别
from clang.cindex import Cursor

import clang.cindex
import subprocess
import os


class CxxParser(Parser):
    __absLibClangSoPath = ""

    def __init__(self):
        super(CxxParser, self).__init__()
        self.__absLibClangSoPath = self.llvmLibDir() + os.sep + 'libclang.so'
        Config.set_library_file(self.__absLibClangSoPath)

    def doParse(self, storage, files, file):
        super(CxxParser, self).doParse(storage, files, file)
        index = clang.cindex.Index.create()
        tu = index.parse(file)
        self.doParseCursor(storage, files, tu.cursor)

    def language(self):
        return ['C', 'C++']

    def mimetypes(self):
        return ['text/x-chdr', 'text/x-c++hdr', 'text/x-csrc', 'text/x-c++src']

    def rootName(self):
        return 'Cxx'

    def llvmLibDir(self):
        """ get llvm lib save dir path
        :return: str llvm-config execute stdout path from lib directory
        """
        proc = subprocess.Popen(["llvm-config", "--libdir"], shell=False,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        proc.wait(1)
        line = proc.stdout.readline()
        if proc.returncode == 0:
            log(__name__).critical("llvm configure lib directory:" + str(line, encoding="utf-8"))
        return str(line, encoding="utf-8").replace('\n', '')

    def getDefaultKindFilter(self):
        return {
            "TRANSLATION_UNIT": [
                "NAMESPACE",
                "STRUCT_DECL",
                "CLASS_DECL",
                "UNION_DECL",
                "TYPEDEF_DECL",
                "FUNCTION_DECL",
            ],
            "STRUCT_DECL": [
                "STRUCT_DECL",
                "FIELD_DECL"
            ],
            "UNION_DECL": [
                "FIELD_DECL"
            ],
            "CLASS_DECL": [
                "CLASS_DECL",
                "UNION_DECL",
                "STRUCT_DECL",
                "TYPEDEF_DECL",
                "FIELD_DECL",
                "CXX_METHOD"
            ],
            "NAMESPACE": [
                "NAMESPACE",
                "CLASS_DECL",
                "UNION_DECL",
                "STRUCT_DECL",
                "TYPEDEF_DECL",
                "FIELD_DECL",
                "CXX_METHOD"
            ]
        }

    def getCursorDirName(self, cursor):
        find_name = cursor.spelling
        cursor_type = cursor.type.spelling
        cursor_kind_name = cursor.kind.name
        if cursor_kind_name == "FIELD_DECL":
            find_name = cursor_type + " " + cursor.spelling
        elif cursor_kind_name == "CXX_METHOD":
            find_name = cursor_type + " " + cursor.spelling
        elif cursor_kind_name == "NAMESPACE":
            find_name = "namespace " + cursor.spelling
        elif cursor_kind_name == "STRUCT_DECL":
            find_name = "struct " + cursor.spelling
        elif cursor_kind_name == "CLASS_DECL":
            find_name = "class " + cursor.spelling
        elif cursor_kind_name == "UNION_DECL":
            find_name = "union " + cursor.spelling
        else:
            pass
        return find_name

    def getCursorDirPath(self, storage, cursor):
        if cursor:
            suffix_path = os.sep + self.getCursorDirName(cursor)
            parent_cursor = cursor.semantic_parent
            while parent_cursor.kind.name != "TRANSLATION_UNIT":
                suffix_path = os.sep + self.getCursorDirName(parent_cursor) + suffix_path
                parent_cursor = parent_cursor.semantic_parent
            return storage + suffix_path
        else:
            return storage

    def doParseCursor(self, storage, files, cursor):
        abs_storage_path = os.path.abspath(storage)
        kind_filter = self.getDefaultKindFilter()
        parent_cursor = cursor.semantic_parent
        translation_unit_file = cursor.translation_unit.spelling
        if parent_cursor:
            cursor_file = cursor.location.file.name
            #  and cursor_file in files
            if parent_cursor.kind.name in kind_filter.keys() \
                    and cursor.kind.name in kind_filter[parent_cursor.kind.name] \
                    and cursor_file in files:
                cursor_map_path = self.getCursorDirPath(abs_storage_path, cursor)
                if not os.path.exists(cursor_map_path):
                    os.mkdir(cursor_map_path)
                #     os.mkdir(abs_storage_path)
                # os.mkdir()
                # os.mkdir(self.findPath(parent_cursor, cursor))
                # print(kind_filter[parent_cursor.kind.name], cursor.kind.name)
                # print("cursor.kind.name", cursor.kind.name)
                print("semantic_parent", cursor.semantic_parent.spelling)
                print("translation_unit:", cursor.translation_unit.spelling)
                print("cursor_file:", cursor.location.file.name)
                print("extent start:", cursor.extent.start)
                print("extent end:", cursor.extent.end)
                print("this_cursor:", cursor.spelling)
                print("line:", cursor.location.line,
                      "col:", cursor.location.column,
                      "kind.name:", cursor.kind.name,
                      "displayName:", cursor.displayname,
                      "type.spelling:", cursor.type.spelling,
                      "type.kind:", cursor.type.kind.name)
                print("")
        for next_cursor in cursor.get_children():
            self.doParseCursor(storage, files, next_cursor)
# if cursor.kind.is_reference():
#     cursor_file = os.path.abspath(location.file.name)
#     if cursor_file in file:
#         print("cursor_file:", cursor_file)
#         print("this_file:", file)
#         print("line:", location.line,
#               "col:", location.column,
#               "kind:", cursor.kind,
#               "displayName:", cursor.displayname,
#               "type.spelling:", cursor.type.spelling,
#               "type.kind:", cursor.type.kind)
#         print("\n")

# Recurse for children of this node


# for cursor in cursor.get_children():
#     location = cursor.location
#     cursor_file = os.path.abspath(location.file.name)
#     if os.path.abspath(file) == cursor_file or cursor_file in file:
#         print("cursor_file:", cursor_file)
#         print("line:", location.line,
#               "col:", location.column,
#               "kind:", cursor.kind,
#               "displayName:", cursor.displayname)
# self.doParseCursor(storage, files, file, cursor)

# if cursor.kind.is_reference():
#     # ref_node = clang.cindex.Cursor_ref(cursor)
#     # if ref_node.spelling == typename:

# print(cursor.kind)
# print(Cursor.location)
# print(cursor.location)
# print(cursor.spelling)
# print(cursor.displayname)
#
#
# if node.kind.is_reference():
#     ref_node = clang.cindex.Cursor_ref(node)
#         print(location.line, location.column, cursor.kind, cursor.displayname)
# # Recurse for children of this node
# for c in node.get_children():
#     self.parser_cursor(c)
