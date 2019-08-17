#
# 33. N-Queens
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.'
# both indicate a queen and an empty space respectively.


class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """

    def solveNQueens(self, n):
        # write your code here
        if not n:
            return []

        self.column_visited = set()
        self.sum_visited = set()
        self.difference_visited = set()
        results = []
        self.solve(n, 0, [], results)
        return results

    def solve(self, n, row, temp_results, results):
        if row == n:
            results.append(self.draw(temp_results, n))
            return

        for col in range(n):
            if not self.check_visited(row, col):
                temp_results.append(col)
                self.sum_visited.add(row + col)
                self.difference_visited.add(row - col)
                self.column_visited.add(col)
                self.solve(n, row + 1, temp_results, results)
                temp_results.pop()
                self.sum_visited.remove(row + col)
                self.difference_visited.remove(row - col)
                self.column_visited.remove(col)

    def check_visited(self, row, col):

        return row + col in self.sum_visited or \
               row - col in self.difference_visited \
               or col in self.column_visited

    def draw(self, temp_results, n):
        results = []
        for row_index in range(n):
            column_str_list = ["."] * n
            column_str_list[temp_results[row_index]] = "Q"
            results.append(''.join(column_str_list))
        return results
