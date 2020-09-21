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
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """

    def closestKValues(self, root, target, k):
        # write your code here
        self.answer_list = []
        self.inorder_stack = self.get_inorder(root)
        left_index = self.get_left_index(target)
        right_index = left_index + 1
        length = len(self.inorder_stack)

        if left_index < 0:
            self.answer_list = self.inorder_stack[:k]
        elif right_index >= length:
            self.answer_list = self.inorder_stack[length - k:]
        else:
            while k > 0:
                left = self.inorder_stack[left_index]
                right = self.inorder_stack[right_index]
                if self.left_closer(left, right, target):
                    self.answer_list.append(left)
                    left_index -= 1
                else:
                    self.answer_list.append(right)
                    right_index += 1
                k -= 1

        return self.answer_list

    def get_inorder(self, root):
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        inorder_stack = []
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                inorder_stack.append(stack[-1].val)
        return inorder_stack

    def get_left_index(self, target):
        start = 0
        end = len(self.inorder_stack) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.inorder_stack[mid] < target:
                start = mid
            elif self.inorder_stack[mid] > target:
                end = mid
            else:
                end = mid

        if self.inorder_stack[end] < target:
            return end

        if self.inorder_stack[start] < target:
            return start

        return -1

    def left_closer(self, left, right, target):
        return abs(target - left) < abs(right - target)