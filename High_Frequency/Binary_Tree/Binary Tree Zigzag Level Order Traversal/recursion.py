# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.height = -1
        self.result = deque([])
        self.helper(root, 0)
        return list(self.result)

    def helper(self, root, height):
        if not root:
            return

        if height > self.height:
            self.height = height
            self.result.append(deque([]))

        if height % 2 == 0:
            self.result[height].append(root.val)
        else:
            self.result[height].appendleft(root.val)

        height += 1

        self.helper(root.left, height)
        self.helper(root.right, height)
