class MyTreeNode:
    """
    @param val: the node's val
    @return: a MyTreeNode object
    """
    def __init__(self, val):
        # write your code here
        self.val = val
        self.parent = None
        self.children = []
        self.is_deleted = False

    """
    @param root: the root treenode
    @return: get the traverse of the treenode
    """
    def traverse(self, root):
        # write your code here
        result = []
        self.helper(root, result)
        return result

    def helper(self, root, result):
        if not root.is_deleted:
            result.append(root.val)
        for node in root.children:
            self.helper(node, result)

    """
    @param root: the node where added
    @param value: the added node's value
    @return: add a node, return the node
    """
    def addNode(self, root, value):
        # write your code here
        node = MyTreeNode(value)
        root.children.append(node)
        node.parent = root
        return node

    """
    @param root: the deleted node
    @return: nothing
    """
    def deleteNode(self, root):
        # write your code here
        root.is_deleted = True