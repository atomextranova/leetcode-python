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
        self.pre = None
        self.dfs(root, p)
        return self.pre

    def dfs(self, root, p):
        if not root:
            return
        if root.val <= p.val:
            self.dfs(root.right, p)

        else:
            self.pre = root
            self.dfs(root.left, p)