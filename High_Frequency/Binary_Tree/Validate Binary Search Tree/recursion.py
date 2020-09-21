# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.helper(root, float('inf'), float('-inf'))

    # Need to keep track of max_val until now to make sure left
    # subtree of children in the right of a node has smaller value than that node

    # Cases:
    # duplicates: False
    # incomplete trees: True
    def helper(self, node, max_val, min_val):

        if not node:
            return True

        if node.val >= max_val or node.val <= min_val:
            return False

        # For left children, node.val is upper bound
        # For right children, node.val is lower bound
        valid = self.helper(node.left, node.val, min_val) and self.helper(
            node.right, max_val, node.val)

        return valid
