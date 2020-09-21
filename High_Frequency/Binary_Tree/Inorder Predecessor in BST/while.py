class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        pre = None
        while root:
            if root.val >= p.val:
                root = root.left

            else:
                if pre is None or root.val > pre.val:
                    pre = root
                root = root.right

        return pre