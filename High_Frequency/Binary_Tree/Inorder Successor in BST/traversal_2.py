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
        next_node = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                if root.val > p.val:
                    next_node = root
                root = root.left

        return next_node
