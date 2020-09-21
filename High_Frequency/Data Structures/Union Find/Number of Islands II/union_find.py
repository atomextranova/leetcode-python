"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        # write your code here
        self.initialize(n * m)
        islands = set()
        results = []
        DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for operator in operators:
            x, y = operator.x, operator.y
            if (x, y) in islands:
                results.append(self.size)
                continue
            islands.add((x, y))
            self.size += 1
            index = self.pos_to_index(x, y, m, n)
            for dx, dy in DIR:
                new_x = x + dx
                new_y = y + dy
                if (new_x, new_y) in islands:
                    new_index = self.pos_to_index(new_x, new_y, m, n)
                    self.union(index, new_index)

            results.append(self.size)
        return results


    def initialize(self, count):
        self.fathers = [i for i in range(count)]
        self.size = 0

    def pos_to_index(self, x, y, m, n):
        return x * m + y

    def find(self, i):
        path = []
        while self.fathers[i] != i:
            path.append(i)
            i = self.fathers[i]

        for p in path:
            self.fathers[p] = i

        return i

    def union(self, i, j):
        if i == j:
            return

        a = self.find(i)
        b = self.find(j)

        if a != b:
            self.fathers[a] = b
            self.size -= 1
