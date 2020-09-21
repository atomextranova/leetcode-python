class SegmentTree(object):
    # 总结
    # 区间操作，修改值或者一段的值
    # 询问区间性质：最大，最小，和。。
    def __init__(self, start, end, cur_sum=0):
        self.start = start
        self.end = end
        self.cur_sum = cur_sum
        self.left = self.right = None

    @classmethod
    def build(cls, start, end, array):
        if start > end:
            return None

        node = SegmentTree(start, end, array[start])

        if start == end:
            return node

        mid = (start + end) // 2
        left = cls.build(start, mid, array)
        right = cls.build(mid + 1, end, array)
        node.left = left
        node.right = right

        node.cur_sum = left.cur_sum + right.cur_sum
        return node

    @classmethod
    def modify(cls, index, value, root):
        if root is None:
            return

        if root.start == root.end:
            root.cur_sum = value
            return

        if root.left.end >= index:
            cls.modify(index, value, root.left)
        else:
            cls.modify(index, value, root.right)
        root.cur_sum = root.left.cur_sum + root.right.cur_sum
        return

    @classmethod
    def query(cls, start, end, root):
        if root.start > end or root.end < start:
            return 0

        if start <= root.start and root.end <= end:
            return root.cur_sum

        return cls.query(start, end, root.left) + \
               cls.query(start, end, root.right)


class Solution:
    """
    @param: A: An integer array
    """

    def __init__(self, A):
        # do intialization if necessary
        self.root = SegmentTree.build(0, len(A) - 1, A)

    """
    @param: start: An integer
    @param: end: An integer
    @return: The sum from start to end
    """

    def query(self, start, end):
        # write your code here
        return SegmentTree.query(start, end, self.root)

    """
    @param: index: An integer
    @param: value: An integer
    @return: nothing
    """

    def modify(self, index, value):
        # write your code here
        SegmentTree.modify(index, value, self.root)