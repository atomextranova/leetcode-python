# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.max_level = 0

    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        self.helper(root, result, 1)
        return result

    def helper(self, root, result, level):

        if not root:
            return
        # check if this encountered at this level
        if level > self.max_level:
            result.append(root.val)
            self.max_level = level

        # Traverse top_down, right->left
        self.helper(root.right, result, level + 1)

        self.helper(root.left, result, level + 1)

