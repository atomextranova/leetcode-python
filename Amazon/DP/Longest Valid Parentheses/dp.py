class Solution:
    """
    @param s: a string
    @return: return a integer
    """

    def longestValidParentheses(self, s):
        # write your code here
        if len(s) <= 1:
            return 0

        dp = [0] * len(s)
        max_len = 0
        for i in range(len(s) - 2, -1, -1):
            if s[i] == ")":
                continue

            right_index = i + dp[i + 1] + 1
            if right_index < len(s) and s[right_index] == ")":
                dp[i] = dp[i + 1] + 2
                if right_index + 1 < len(s):
                    dp[i] += dp[right_index + 1]
            max_len = max(dp[i], max_len)
        return max_len