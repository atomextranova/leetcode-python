"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        # write your code here
        self.last = None
        self.result = None
        self.helper(root, p)
        return self.result

    def helper(self, root, p):
        if root is None or self.result is not None:
            return
        self.helper(root.left, p)
        if root == p:
            self.result = self.last
        self.last = root
        self.helper(root.right, p)