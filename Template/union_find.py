class UnionFind:

    def __init__(self, n):
        self.father = {}
        for i in range(n):
            self.father[i] = i
        self.rank = {}
        for i in range(n):
            self.rank[i] = 1

    # Path compression
    def find(self, a):
        # if self.father[a] != a:
        #     self.father[a] = self.find(self.father[a])
        # return self.father[a]

        # Iterative
        path = []
        while self.father[a] != a:
            path.append(a)
            a = self.father[a]
        for n in path:
            self.father[n] = a
        return a

    def union(self, a, b):
        # Naive

        father_a = self.find(a)
        father_b = self.find(b)
        if father_a != father_b:
            self.father[father_a] = father_b
        #     size - 1 if count size

        # father_a = self.find(a)
        # father_b = self.find(b)

        # if father_a != father_b:
        #     if self.rank[father_a] < self.rank[father_b]:
        #         self.father[father_a] = father_b
        #     elif self.rank[father_a] > self.rank[father_b]:
        #         self.father[father_b] = father_a
        #     else:
        #         self.father[father_b] = father_a
        #         self.rank[father_a] += 1


