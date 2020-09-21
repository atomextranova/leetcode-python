# 1. DFS inroder, return if root == None
# 2. 如果first为空，first和last指向当前node
# 3. last right指向当前node, 当前left指向last,last = node
# 4. 最后更新first和last

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        self.first = None
        self.last = None
        self.helper(root)
        self.first.left = self.last
        self.last.right = self.first
        return self.first

    def helper(self, root):
        if not root:
            return

        self.helper(root.left)

        if not self.first:
            self.first = root
            self.last = root
        else:
            self.last.right = root
            root.left = self.last
            self.last = root

        self.helper(root.right)