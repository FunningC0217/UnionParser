
class SyntaxTreeNode:
    src_file_path = ""
    prefix_len = 0
    type = ""
    string = ""
    range = []
    parent = None
    child = list()


def findParent(root: SyntaxTreeNode, prefix_len: int) -> SyntaxTreeNode:
    if prefix_len < 0:
        return None

    if prefix_len == 0:
        return root

    if prefix_len == root.prefix_len:
        return root.parent

    for node in reversed(root.child):
        return findParent(node, prefix_len)

    return root
