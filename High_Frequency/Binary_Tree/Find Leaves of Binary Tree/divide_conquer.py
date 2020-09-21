"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """

    def findLeaves(self, root):
        # write your code here
        if not root:
            return []
        self.leaves = []
        self.leaves_helper(root)
        return self.leaves

    # recursion, keep track of height (bot = 0, root = max_height),
    # self.leaves = []
    # create list for each new height seen, where height = max(left, right) + 1
    # insert value B
    def leaves_helper(self, node):

        if not node:
            return -1

        left_height = self.leaves_helper(node.left)
        right_height = self.leaves_helper(node.right)
        cur_height = max(left_height, right_height) + 1
        if len(self.leaves) <= cur_height:
            self.leaves.append([])
        self.leaves[cur_height].append(node.val)
        return cur_height

