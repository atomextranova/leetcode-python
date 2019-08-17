class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        # write your code here
        dp_table = [[0] * n for _ in range(m)]

        dp_table[0][0] = 1
        for i in range(1, n):
            dp_table[0][i] = 1

        for i in range(1, m):
            dp_table[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp_table[i][j] = dp_table[i - 1][j] + dp_table[i][j - 1]

        return dp_table[m - 1][n - 1]