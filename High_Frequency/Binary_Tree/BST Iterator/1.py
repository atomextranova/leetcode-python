from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        dummy = TreeNode(0)
        dummy.right = root
        self.stack = [dummy]
        self.next()

    def next(self) -> int:
        """
        @return the next smallest number
        """

        root = self.stack.pop()
        next_node = root
        if root.right:
            root = root.right
            while root:
                self.stack.append(root)
                root = root.left
        return next_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) != 0