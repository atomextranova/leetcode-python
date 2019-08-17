"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """

    def __init__(self, root):
        # do intialization if necessary

        dummy = TreeNode(0)
        dummy.right = root
        self.stack = [dummy]
        self.next()

    """
    @return: True if there has next node, or false
    """

    def hasNext(self, ):
        # write your code here
        return len(self.stack) != 0

    """
    @return: return next node
    """

    def next(self, ):
        # write your code here
        temp_node = self.stack.pop()
        next_node = temp_node
        if temp_node.right:
            temp_node = temp_node.right
            while temp_node:
                self.stack.append(temp_node)
                temp_node = temp_node.left
        return next_node


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node2.left = node1
node2.right = node3

iterator = BSTIterator(node2)
while iterator.hasNext():
    node = iterator.next()
    print(node.val)
