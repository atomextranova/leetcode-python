"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the new root
    """

    # Traversal order: right->root->left (post)
    # root.val = cur_sum (Sum of all nodes before it)
    # cur_sum += root.val
    def convertBST(self, root):
        # write your code here
        self.cur_sum = 0
        if not root:
            return
        self.modify(root)
        return root

    def modify(self, root):
        if not root:
            return

        self.modify(root.right)
        self.cur_sum += root.val
        root.val = self.cur_sum
        self.modify(root.left)