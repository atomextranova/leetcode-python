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
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        # write your code here
        valid, _, _ = self.helper(root)
        return valid

    def helper(self, root):
        if not root:
            return True, None, None

        left_valid, left_max, left_min = self.helper(root.left)
        right_valid, right_max, right_min = self.helper(root.right)

        if not left_valid or not right_valid:
            return False, None, None

        root_left_valid = False
        root_right_valid = False

        if left_max is None or left_max < root.val:
            root_left_valid = True

        if right_min is None or right_min > root.val:
            root_right_valid = True

        # return root val if None
        if right_max is None:
            right_max = root.val

        if left_min is None:
            left_min = root.val

        return root_left_valid and root_right_valid, right_max, left_min
