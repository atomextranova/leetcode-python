import numpy as np

class Solution(object):
    # 2D DP, could use 1D
    # Initial
    # dp[0][0] stands for empty string, always true
    # State:
    # dp[i][j] stands for whether (s1[:i+1] and s2[:j]) or (s1[:i] and s2[:j+1])
    # could form a interleaving of s3[:i+j]
    # Transition:
    # dp_table[i][j] = (dp_table[i - 1][j] and s2[i - 1] == s3[
    #                     i + j - 1])
    #                     or (dp_table[i][j - 1] and s1[j - 1] ==
    #                     s3[
    #                     i + j - 1])
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        length_1 = len(s1)
        length_2 = len(s2)
        length_3 = len(s3)
        if length_1 + length_2 != length_3:
            return False
        # Could do BFS here, maintain a queue of feasible interleaving
        dp_table = [[False] * (length_1 + 1) for _ in range(length_2 + 1)]
        dp_table[0][0] = True

        for i in range(1, length_1+1):
            dp_table[0][i] = dp_table[0][i - 1] and (s1[i-1] == s3[i-1])

        for i in range(1, length_2+1):
            dp_table[i][0] = dp_table[i - 1][0] and (s2[i-1] == s3[i-1])

        for i in range(1, length_2+1):
            for j in range(1, length_1+1):
                dp_table[i][j] = (dp_table[i - 1][j] and s2[i - 1] == s3[
                    i + j - 1]) or (dp_table[i][j - 1] and s1[j - 1] == s3[
                    i + j - 1])
        # print(dp_table)
        return dp_table[-1][-1]

sol = Solution()
sol.isInterleave("aabcc", "dbbca", s3 = "aadbbcbcac")