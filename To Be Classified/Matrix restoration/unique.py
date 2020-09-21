class Solution:
    """
    @param n: the row of the matrix
    @param m: the column of the matrix
    @param after: the matrix
    @return: restore the matrix
    """

    def matrixRestoration(self, n, m, after):
        # write your code here
        cur_sum = 0

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i > 0:
                    after[i][j] -= after[i - 1][j]
                if j > 0:
                    after[i][j] -= after[i][j - 1]

                if i > 0 and j > 0:
                    after[i][j] += after[i - 1][j - 1]

        return after