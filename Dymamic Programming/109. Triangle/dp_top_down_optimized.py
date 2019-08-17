class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    # O(n^2)
    # Space: O(n^2)
    def minimumTotal(self, triangle):
        # write your code here
        n = len(triangle)
        dp_table = [[0] * n, [0] * n]

        dp_table[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            # leftmost and rightmost path, only 1 path
            # % 2 to use different row of table
            # Only save intermediate result
            dp_table[i % 2][0] = triangle[i][0] + dp_table[(i - 1) % 2][0]
            dp_table[i % 2][i] = triangle[i][i] + dp_table[(i - 1) % 2][i - 1]
            # in the middle, 2 possible paths
            for j in range(1, i):
                left_prev = dp_table[(i - 1) % 2][j - 1]
                right_prev = dp_table[(i - 1) % 2][j]

                dp_table[i % 2][j] = min(left_prev, right_prev) + triangle[i][j]

        return min(dp_table[(len(triangle) - 1) % 2])

sol = Solution()
print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))