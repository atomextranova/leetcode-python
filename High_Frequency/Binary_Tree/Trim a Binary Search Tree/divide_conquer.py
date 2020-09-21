# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # if root.val < L, return divide(root.left)
    # if root.val > R, return divide(root.right)
    # L <= <= R, in mid, deal with child
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None

        return self.divide(root, L, R)

    def divide(self, root, L, R):
        if not root:
            return root

        if root.val < L:
            return self.divide(root.right, L, R)

        if root.val > R:
            return self.divide(root.left, L, R)

        root.left = self.divide(root.left, L, R)
        root.right = self.divide(root.right, L, R)

        return root