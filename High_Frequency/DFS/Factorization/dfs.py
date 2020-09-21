import math

class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        if n == 1:
            return

        self.result = []
        low = 2
        self.dfs(low, n, [])
        return self.result

    def dfs(self, low, n, temp):
        if n == 1:
            if len(temp) > 1:
                self.result.append(temp[:])
            return

        for i in range(low, int(math.sqrt(n) + 1)):
            if n % i != 0:
                continue
            # print(i)
            temp.append(i)
            self.dfs(temp[-1], n // i, temp)
            temp.pop()

        temp.append(n)
        self.dfs(temp[-1], 1, temp)
        temp.pop()
        return


