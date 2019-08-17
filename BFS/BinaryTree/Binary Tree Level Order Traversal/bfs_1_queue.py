"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        # write your code here
        if not root:
            return []
        to_be_visited = deque([root])
        result = []

        while to_be_visited:
            length = len(to_be_visited)
            level_result = []
            for _ in range(length):
                current_node = to_be_visited.popleft()
                if current_node.left:
                    to_be_visited.append(current_node.left)
                if current_node.right:
                    to_be_visited.append(current_node.right)
                level_result.append(current_node.val)
            result.append(level_result)

        return result