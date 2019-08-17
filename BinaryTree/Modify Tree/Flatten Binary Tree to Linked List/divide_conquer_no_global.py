"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def flatten(self, root):
        # write your code here
        self.helper(root)

    def helper(self, root):
        if root is None:
            return None

        left_node = self.helper(root.left)
        right_node = self.helper(root.right)

        if left_node is not None and right_node is not None:
            left_node.right = root.right
            root.right = root.left
            root.left = None
            return right_node

        if left_node is not None:
            root.right = root.left
            root.left = None
            return left_node

        if right_node is not None:
            return right_node

        return root
