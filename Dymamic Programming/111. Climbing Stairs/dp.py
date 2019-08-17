class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here
        if n == 0:
            return n

        dp_table = [0] * (n + 1)
        dp_table[0] = 1
        dp_table[1] = 1

        for i in range(2, n + 1):
            dp_table[i] = dp_table[i - 1] + dp_table[i - 2]

        return dp_table[n]