import sys


class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    # O(n^2)
    # Space: O(n^2)
    def minimumTotal(self, triangle):
        # write your code here
        row_index, col_index = 0, 0
        memo = {}
        max_row = len(triangle) - 1
        return self.dfs(triangle, row_index, col_index, memo, max_row)

    def dfs(self, triangle, row_index, col_index, memo, max_row):

        if (row_index, col_index) in memo:
            return memo[(row_index, col_index)]

        if row_index == max_row:
            return triangle[row_index][col_index]

        min_sum = triangle[row_index][col_index] + \
                  min(self.dfs(triangle, row_index + 1, col_index, memo,
                               max_row),
                      self.dfs(triangle, row_index + 1, col_index + 1, memo,
                            max_row))

        memo[(row_index, col_index)] = min_sum

        return min_sum

sol = Solution()
print(sol.minimumTotal([
     [2],
    [3,2],
   [6,5,7],
  [4,4,8,1]
]))


