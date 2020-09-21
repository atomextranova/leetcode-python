class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """

    def totalNQueens(self, n):
        # write your code here
        self.col = {}
        self.n = n
        self.count = 0
        self.search(0)
        return self.count

    def search(self, row):
        if row == self.n:
            self.count += 1

        for i in range(self.n):
            if self.check_col(i) or self.check_diagonal(row, i):
                continue
            self.col[i] = row
            self.search(row + 1)
            del self.col[i]

    def check_diagonal(self, row, column):
        diff = row - column
        sum_rc = row + column
        for c, r in self.col.items():
            if r - c == diff or r + c == sum_rc:
                return True

        return False

    def check_col(self, column):
        return column in self.col