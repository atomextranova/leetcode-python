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

    # Edge case:
    # Not found
    # root/p empty

    def inorderSuccessor(self, root, p):
        if root is None:
            return None

        if root.val <= p.val:
            