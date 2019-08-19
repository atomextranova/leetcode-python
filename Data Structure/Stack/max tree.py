class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """

    def maxTree(self, A):
        stack = []
        for num in A:
            node = TreeNode(num)  # 新建节点
            while stack and num > stack[-1].val:  # 如果stk中的最后一个节点比新节点小
                node.left = stack.pop()
                print([node.val for node in stack])  # 当前新节点的左子树为stk的最后一个节点

            if stack:  # 如果stk不为空
                stack[-1].right = node
                print([node.val for node in stack])  # 将新节点设为stk最后一个节点的右子树

            stack.append(node)
            print([node.val for node in stack])

        return stack[0]


sol = Solution()
sol.maxTree([2, 5, 6, 0, 3, 1, 7])
