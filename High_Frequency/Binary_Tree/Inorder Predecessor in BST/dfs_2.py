class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        self.pre = None
        self.dfs(root, p)
        return self.pre

    def dfs(self, root, p):
        if not root:
            return
        if root.val >= p.val:
            self.dfs(root.left, p)
        else:
            self.pre = root
            self.dfs(root.right, p)