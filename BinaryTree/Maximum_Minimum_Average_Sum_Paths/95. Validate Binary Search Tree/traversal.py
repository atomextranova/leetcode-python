"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        # write your code here
        valid = self.helper(root)
        return valid

    def helper(self, root):
        if not root:
            return True

        stack = []

        while root:
            stack.append(root)
            root = root.left

        # In order traversal template
        while stack:
            node = stack.pop()
            last_node_val = node.val
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

            if stack:
                # >= instead of >
                if last_node_val >= stack[-1].val:
                    return False

        return True
