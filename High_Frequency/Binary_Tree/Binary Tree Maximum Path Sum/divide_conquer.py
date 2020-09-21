# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 1.recursion
    # 2.当前节点为根节点最大值为左children, 右children中大于0的值之和加上当前node
    # 3.返回左子树 / 右子树中大于0的较大值（或者0如果两边小于0）加上当前node之和
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        self.helper(root)
        return self.max_sum

    def helper(self, root):
        if not root:
            return 0

        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
        max_sum = max(left_sum, right_sum, 0) + root.val
        self.max_sum = max(self.max_sum,
                           max(left_sum, 0) + max(right_sum, 0) + root.val)
        return max_sum