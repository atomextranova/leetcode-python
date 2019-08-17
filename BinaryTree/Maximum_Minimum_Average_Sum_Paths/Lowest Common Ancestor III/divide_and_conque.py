"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        A_current, B_current, parent = self.helper(root, A, B)
        if A_current and B_current:
            return parent
        else:
            return None

    def helper(self, root, A, B):
        if root is None:
            return False, False, None

        left_A, left_B, left_node = self.helper(root.left, A, B)
        right_A, right_B, right_node = self.helper(root.right, A, B)

        A_current = left_A or right_A or root == A
        B_current = left_B or right_B or root == B

        if root == A or root == B:
            return A_current, B_current, root

        if left_node and right_node:
            return A_current, B_current, root

        if left_node:
            return A_current, B_current, left_node

        if right_node:
            return A_current, B_current, right_node

        return False, False, None
