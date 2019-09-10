from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.cur_node = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        # if cur_node is not None
        # try push every left node onto the stack
        while self.cur_node is not None:
            self.stack.append(self.cur_node)
            self.cur_node = self.cur_node.left

        # next_node is stack[-1]
        # cur_node point to next_node.right(may be None
        # indicating next_node is new stack[-1)
        next_node = self.stack.pop()
        self.cur_node = next_node.right
        return next_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.cur_node is not None or len(self.stack) > 0