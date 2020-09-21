class Solution:
    """
    @param n: the row of the matrix
    @param m: the column of the matrix
    @param after: the matrix
    @return: restore the matrix
    """
    def matrixRestoration(self, n, m, after):
        # write your code here

        # before = [[0] * m for _ in range(n)]
        # before[0][0] = after[0][1]
        for i in range(n - 1, 0, -1):
            for j in range(m - 1, 0, -1):
                after[i][j] -= after[i][j-1] + after[i-1][j] - after[i-1][j-1]

        for i in range(n - 1, 0, -1):
            after[i][0] -= after[i-1][0]

        for i in range(m - 1, 0, -1):
            after[0][i] -= after[0][i-1]

        return after