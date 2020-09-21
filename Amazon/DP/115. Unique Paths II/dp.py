class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp_table = [[0] * n for _ in range(m)]

        dp_table[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(1, n):
            if obstacleGrid[0][i] == 0:
                dp_table[0][i] = dp_table[0][i - 1]

        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp_table[i][0] = dp_table[i-1][0]

        # dp[i][j] = dp[i - 1][j] + dp[i][j - 1]。
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp_table[i][j] = dp_table[i - 1][j] + dp_table[i][j - 1]

        return dp_table[m - 1][n - 1]

sol = Solution()
sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])