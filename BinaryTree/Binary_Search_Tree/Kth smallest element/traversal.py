class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):
        # write your code here
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        for i in range(k):
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    # 顺序不可变
                    stack.append(node)
                    node = node.left
            # break needed
            if not stack:
                break

        return stack[-1].val
