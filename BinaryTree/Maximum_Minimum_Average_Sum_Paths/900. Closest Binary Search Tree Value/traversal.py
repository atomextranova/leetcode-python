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
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root, target):
        # write your code here

        if not root:
            return -1

        lower = root.val
        upper = root.val

        while root:
            root_val = root.val
            if root_val < target:
                lower = root_val
                root = root.right
            elif root_val > target:
                upper = root_val
                root = root.left
            else:
                return root_val

        if abs(target - lower) < abs(target - upper):
            return lower
        else:
            return upper
