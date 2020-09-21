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
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber3(self, root):
        # write your code here
        return max(self.dfs(root))

    def dfs(self, root):
        if root == None:
            return 0, 0

        left_selected, left_not = self.dfs(root.left)
        right_selected, right_not = self.dfs(root.right)

        return left_not + right_not + root.val, max(left_not, left_selected) + max(right_not, right_selected)