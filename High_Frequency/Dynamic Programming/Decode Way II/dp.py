class Solution:
    """
    @param s: a message being encoded
    @return: an integer
    """
    def numDecodings(self, s):
        # write your code here
        if not s:
            return 0

        MOD = int(1e9 +7)
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s) + 1):
            char = s[i - 1]
            if char == "*":
                dp[i] = (dp[i] + dp[i - 1] * 9) % MOD
            elif int(char) > 0:
                dp[i] = (dp[i] + dp[i - 1]) % MOD

            if i > 1:
                if s[i - 2] == "1":
                    if char == "*":
                        dp[i] = (dp[i] + dp[i - 2] * 9) % MOD
                    else:
                        dp[i] = (dp[i] + dp[i - 2]) % MOD
                elif s[i - 2] == "2":
                    if char == "*":
                        dp[i] = (dp[i] + dp[i - 2] * 6) % MOD
                    elif int(char) <=6:
                        dp[i] = (dp[i] + dp[i - 2]) % MOD
                elif s[i - 2] == "*":
                    if char == "*":
                        dp[i] = (dp[i] + dp[i - 2] * 15) % MOD
                    elif int(char) <= 6:
                        dp[i] = (dp[i] + dp[i - 2] * 2) % MOD
                    else:
                        dp[i] = (dp[i] + dp[i - 2]) % MOD

        return dp[-1]




