"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree.
    @return: true if it is a mirror of itself, or false.
    """

    def isSymmetric(self, root):
        # write your code here
        if not root:
            return True

        return self.helper(root.left, root.right)

    def helper(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False

        return self.helper(root1.left, root2.right) and self.helper(root1.right,
                                                                    root2.left)