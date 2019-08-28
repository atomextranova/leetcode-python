"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: new root
    """

    def upsideDownBinaryTree(self, root):
        # write your code here
        if not root:
            return root

        return self.helper(root)

    def helper(self, root):
        if root.left is None:
            return root

        new_root = self.helper(root.left)
        root.left.right = root
        root.left.left = root.right
        root.left = None
        root.right = None

        return new_root
