"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        self.last = None
        self.result = None
        self.helper(root, p)
        return self.result

    def helper(self, root, p):
        if root is None or self.result is not None:
            return

        self.helper(root.right, p)
        if root == p:
            self.result = self.last

        self.last = root
        self.helper(root.left, p)