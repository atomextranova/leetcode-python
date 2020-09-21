"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        if not root:
            return None
        new = TreeNode(float('-inf'))
        new.right = root
        pre = None
        stack = [new]
        while stack:
            next_root = stack.pop()

            if(next_root.val == p.val):
                return pre if pre.val != float('-inf') else None
            pre = next_root

            if next_root.right:
                next_root = next_root.right
                while next_root:
                    stack.append(next_root)
                    next_root = next_root.left

        return pre if pre.val != float('-inf') else None