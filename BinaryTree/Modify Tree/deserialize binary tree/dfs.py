# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root or root.val == None:
            return ""

        str_list = []
        self.serialize_helper(root, str_list)
        data = ",".join(str_list)
        return data

    def serialize_helper(self, root, str_list):
        if not root:
            str_list.append("N")
            return

        str_list.append(str(root.val))
        self.serialize_helper(root.left, str_list)
        self.serialize_helper(root.right, str_list)

        return

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data or data == "N":
            return []
        data_list = data.split(",")
        # could return instead
        self.index = 0
        return self.deserialize_helper(data_list, len(data_list))

    def deserialize_helper(self, str_list, length):
        if self.index < length:
            val = str_list[self.index]
            self.index += 1
            if val == "N":
                return None
            node = TreeNode(val)
            node.left = self.deserialize_helper(str_list, length)
            node.right = self.deserialize_helper(str_list, length)
            return node
        else:
            return None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))