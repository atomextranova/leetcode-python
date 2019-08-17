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
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        # write your code here
        _, _, min_root = self.findSubtreeHelper(root)
        return min_root

    def findSubtreeHelper(self, root):
        if root is None:
            return sys.maxsize, 0, root

        left_minimum, left_sum, left_root = self.findSubtreeHelper(root.left)
        right_minimum, right_sum, right_root = self.findSubtreeHelper(
            root.right)
        total_sum = left_sum + right_sum + root.val
        min_sum = min(left_minimum, right_minimum, total_sum)
        if left_minimum == min_sum:
            return left_minimum, total_sum, left_root
        elif right_minimum == min_sum:
            return right_minimum, total_sum, right_root
        else:
            return total_sum, total_sum, root
