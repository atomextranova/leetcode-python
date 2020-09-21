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
    # Traverse top down, right to left, check depth at each node
    # The right side view contains node which has depth larger than
    # all nodes before it when traversing in this order

    # 1.DFS, divide and conquer
    # 2.top - down, right to left
    # 3.self.max_level = 0
    # 4.record level, for every level > max_level,
    #     that node is on the right, max_level = level
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

