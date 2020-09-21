class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, A, m):
        # write your code here
        if m == 0 or len(A) == 0:
            return 0

        dp = [0 for _ in range(m + 1)]
        dp[0] = 1
        for i in range(len(A)):
            for j in range(m, A[i] - 1, -1):
                dp[j] += dp[j - A[i]]

        return dp[-1]
