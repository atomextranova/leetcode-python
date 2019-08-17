"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # write your code here
        if root is None:
            return []
        current_path_list = []
        current_path_list.append(str(root.val))
        result = []
        self.binaryTreePathHelper(root, current_path_list, result)
        return result

    def binaryTreePathHelper(self, root, current_path_list, result):
        if root.left is None and root.right is None:
            result.append("->".join(current_path_list))
            return

        if root.left is not None:
            current_path_list.append(str(root.left.val))
            self.binaryTreePathHelper(root.left, current_path_list, result)
            current_path_list.pop()

        if root.right is not None:
            current_path_list.append(str(root.right.val))
            self.binaryTreePathHelper(root.right, current_path_list, result)
            current_path_list.pop()
