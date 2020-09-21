class Solution(object):
    def prisonAfterNDays(self, cells, N):
        if N <= 0:
            return cells

        self.memo = {}

        new = [0] * 8
        # new, cells = self.simulate(cells, new)
        # new[0] = 0
        # new[7] = 0

        while N > 0:
            old_tuple = tuple(cells)
            if old_tuple in self.memo:
                N %= self.memo[old_tuple] - N
            self.memo[old_tuple] = N
            if N >= 1:
                N -= 1
                new, cells = self.simulate(cells, new, old_tuple)
            # print(cells)
        return cells

    def simulate(self, old, new, old_tuple):
        new[0] = 0
        new[7] = 0
        for i in range(1, 7):
            new[i] = (old[i - 1] ^ old[i + 1]) ^ 1
        # self.memo[old_tuple] = new
        return old, new