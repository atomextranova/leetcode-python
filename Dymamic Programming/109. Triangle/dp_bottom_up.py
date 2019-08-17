class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    # O(n^2)
    # Space: O(n^2)
    def minimumTotal(self, triangle):
        # write your code here

        length = len(triangle)
        dp_table = [[0] * i for i in range(1, length + 1)]

        for i in range(length):
            dp_table[length - 1][i] = triangle[length - 1][i]

        for i in range(length - 2, -1, -1):
            for j in range(i + 1):
                left_prev = dp_table[i+1][j]
                right_prev = dp_table[i+1][j+1]

                dp_table[i][j] = min(left_prev, right_prev) + triangle[i][j]

        return dp_table[0][0]