"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        valid, _ = self.helper(root)
        return valid

    def helper(self, root):
        if not root:
            return True, 1

        # could return early if left not valid without checking right
        left_valid, left_height = self.helper(root.left)
        right_valid, right_height = self.helper(root.right)

        if not left_valid or not right_valid:
            return False, None

        return abs(left_height - right_height) <= 1, max(left_height,
                                                         right_height) + 1
