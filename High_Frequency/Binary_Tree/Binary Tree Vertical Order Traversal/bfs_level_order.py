# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque


class Solution:
    def __init__(self):
        self.index_to_nodes = defaultdict(list)
        self.min_index = float('inf')
        self.max_index = float('-inf')

    # use min_index/max_index to keep track of vertical index range
    # store list of node in a dict with different vertical indexes as keys
    # Use queue, keep track of vertical index, add child nodes to the queue
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        self.helper(root)
        for i in range(self.min_index, self.max_index + 1):
            result.append(list(self.index_to_nodes[i]))
        return result

    def helper(self, root):
        queue = deque([(root, 0)])

        while queue:
            for i in range(len(queue)):
                node, index = queue.popleft()
                self.min_index = min(self.min_index, index)
                self.max_index = max(self.max_index, index)
                self.index_to_nodes[index].append(node.val)
                if node.left:
                    queue.append((node.left, index - 1))
                if node.right:
                    queue.append((node.right, index + 1))

