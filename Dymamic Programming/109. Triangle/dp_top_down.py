class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    # O(n^2)
    # Space: O(n^2)
    def minimumTotal(self, triangle):
        # write your code here
        dp_table = [[0] * i for i in range(1, len(triangle) + 1)]

        dp_table[0][0] = triangle[0][0]

        # leftmost and rightmost path
        for i in range(1, len(triangle)):
            dp_table[i][0] = triangle[i][0] + dp_table[i - 1][0]
            dp_table[i][i] = triangle[i][i] + dp_table[i - 1][i - 1]

        for i in range(2, len(triangle)):
            for j in range(1, i):
                left_prev = dp_table[i - 1][j - 1]
                right_prev = dp_table[i - 1][j]

                dp_table[i][j] = min(left_prev, right_prev) + triangle[i][j]

        return min(dp_table[len(triangle) - 1])


sol = Solution()
print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))