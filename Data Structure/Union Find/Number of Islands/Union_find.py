
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b



class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """

    # Edge case:
    # A not in range
    # Repeat elements

    def numIslands2(self, n, m, operators):
        # write your code here
        self.m = m
        self.n = n
        length = n * m
        self.initialize(length)

        result = []
        self.island_size = 0
        delta_x = (-1, 1, 0, 0)
        delta_y = (0, 0, 1, -1)
        islands = set()
        for i, operator in enumerate(operators):
            x, y = operator.x, operator.y
            if (x, y) in islands:
                result.append(self.island_size)
                continue
            islands.add((x, y))
            # Always increase first
            # If union happens, union() deals with size count
            self.island_size += 1
            for dx, dy in zip(delta_x, delta_y):
                new_x = x + dx
                new_y = y + dy
                if (new_x, new_y) in islands:
                    self.union(new_x, new_y, x, y)
            result.append(self.island_size)

        return result

    def pos_to_index(self, x, y, m, n):
        return x * m + y

    def initialize(self, length):
        self.father = []

        for i in range(length):
            self.father.append(i)

    def find(self, target):
        if self.father[target] != target:
            self.father[target] = self.find(self.father[target])
        return self.father[target]

    def union(self, ax, ay, bx, by):
        a = self.pos_to_index(ax, ay, self.m, self.n)
        b = self.pos_to_index(bx, by, self.m, self.n)
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.father[root_a] = root_b
            # -1 if union happened
            self.island_size -= 1


n = 10
m = 17
operators = [[5, 5], [0, 7], [1, 13], [5, 14], [7, 15], [3, 15], [2, 10],
             [4, 6], [4, 9], [1, 2], [3, 13], [4, 8], [9, 15], [6, 4], [6, 11],
             [9, 11], [0, 16], [3, 6], [3, 14], [6, 1], [7, 13], [2, 0], [6, 0],
             [6, 9], [7, 1], [7, 4], [5, 15], [0, 1], [1, 16], [6, 16], [5, 6],
             [3, 12], [9, 1], [7, 2], [8, 2], [6, 2], [6, 8], [4, 7], [1, 15],
             [3, 0], [5, 10], [9, 9], [8, 1], [8, 4], [9, 2], [3, 11], [6, 6],
             [2, 16], [9, 5], [2, 4], [9, 13], [3, 16], [7, 14], [2, 3],
             [8, 13], [7, 10], [9, 4], [8, 16], [4, 12], [3, 2], [1, 0], [1, 9]]

