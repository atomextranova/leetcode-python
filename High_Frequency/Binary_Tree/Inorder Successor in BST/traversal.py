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
        # write your code here
        if not root or not p:
            return None

        parent = None
        while root is not None and root.val != p.val:
            if root.val > p.val:
                parent = root
                root = root.left
            if root.val < p.val:
                root = root.right

        if not root:
            return None

        if root.right:
            root = root.right
            while root.left:
                root = root.left
            return root
        else:
            return parent


