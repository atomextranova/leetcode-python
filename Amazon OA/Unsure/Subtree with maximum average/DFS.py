class TreeNode:
    def __init__(self, value):
        self.val = value
        self.children = []


class Solution:
    def MaxAverageSubtree(self, root):
        if not root or not root.children:
            return None

        self.res = [float('-inf'), 0]
        # self.res[0]: average; self.res[1]: number of nodes
        self.dfs(root)
        return self.res[1]

    def dfs(self, root):
        if not root.children:
            return [root.val, 1]

        temp_sum, temp_num = root.val, 1
        for child in root.children:
            child_sum, child_num = self.dfs(child)
            temp_sum += child_sum
            temp_num += child_num

        if temp_sum / temp_num > self.res[0]:
            self.res = [temp_sum / temp_num, root.val]

        return [temp_sum, temp_num]