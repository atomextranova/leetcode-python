class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """

    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp_table = [[0] * n for _ in range(m)]

        dp_table[0][0] = grid[0][0]
        for i in range(1, n):
            dp_table[0][i] = grid[0][i] + dp_table[0][i - 1]

        for i in range(1, m):
            dp_table[i][0] = grid[i][0] + dp_table[i - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                dp_table[i][j] = min(dp_table[i - 1][j], dp_table[i][j - 1]) + \
                                 grid[i][j]

        return dp_table[m - 1][n - 1]
