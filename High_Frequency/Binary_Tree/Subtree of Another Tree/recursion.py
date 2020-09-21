/# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True

        if not s:
            return False

        # Check exhaustively for each node, node value not unique
        return self.helper(s, t) or self.isSubtree(s.left, t) or self.isSubtree(
            s.right, t)

    def helper(self, s, t):
        if not s and not t:
            return True

        if not s or not t:
            return False

        return s.val == t.val and self.helper(s.left, t.left) and self.helper(
            s.right, t.right)

