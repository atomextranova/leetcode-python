class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):
        # write your code here
        node_count = {}
        self.count_nodes(root, node_count)
        node = self.quick_select(root, node_count, k)
        return node.val

    def count_nodes(self, root, node_count):
        if not root:
            return 0

        left_node_count = self.count_nodes(root.left, node_count)
        right_node_count = self.count_nodes(root.right, node_count)
        total_nodes = left_node_count + right_node_count + 1
        node_count[root] = total_nodes
        return total_nodes

    def quick_select(self, root, node_count, k):
        left_node_count = node_count.get(root.left, 0)
        if (k == left_node_count + 1):
            return root
        elif (k <= left_node_count):
            return self.quick_select(root.left, node_count, k)
        else:
            return self.quick_select(root.right, node_count,
                                     k - left_node_count - 1)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node2.left = node1
node2.right = node3

sol = Solution()
print(sol.kthSmallest(node2, 1).val)
