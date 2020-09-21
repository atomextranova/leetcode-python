# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.result = []
        self.max_height = -1
        self.helper(root, 0)

        return self.result

    def helper(self, root, height):
        if not root:
            return

        if height > self.max_height:
            self.result.append([])
            self.max_height = height

        self.result[height].append(root.val)
        self.helper(root.left, height + 1)
        self.helper(root.right, height + 1)