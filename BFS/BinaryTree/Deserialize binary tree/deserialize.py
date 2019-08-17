class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

from collections import deque


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    # Append left right if current node != None to ensure #
    # Append # string if None
    def serialize(self, root):
        # write your code here
        if not root:
            return ""
        to_be_visited = deque([root])

        result = []
        while to_be_visited:
            length = len(to_be_visited)
            level_result = []
            for _ in range(length):
                current_node = to_be_visited.popleft()
                if current_node:
                    level_result.append(str(current_node.val))
                    to_be_visited.append(current_node.left)
                    to_be_visited.append(current_node.right)
                else:
                    level_result.append("#")
            level_result_str = ",".join(level_result)
            result.append(level_result_str)
        result_str = ".".join(result)
        return result_str

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """

    def deserialize(self, data):
        if data == "":
            return None
        # write your code here
        root = TreeNode(int(data[0]))
        tree_list = [s.split(',') for s in data.split('.')]
        tree_list_length = len(tree_list)
        current_list = [root]
        for index, level_list in enumerate(tree_list):
            if 0 < index <= tree_list_length:
                is_left = True
                current_root = None
                next_list = []
                for leaf_val in level_list:
                    if leaf_val == '#':
                        leaf_node = None
                    else:
                        leaf_node = TreeNode(int(leaf_val))
                        next_list.append(leaf_node)
                    if is_left:
                        current_root = current_list.pop(0)
                        current_root.left = leaf_node
                    else:
                        current_root.right = leaf_node
                    is_left = not is_left
                current_list = next_list
        return root

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol = Solution()
new_root = sol.deserialize(sol.serialize(root))
print(sol.serialize(new_root))