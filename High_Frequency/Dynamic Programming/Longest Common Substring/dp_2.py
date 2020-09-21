class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """

    # State
    def longestCommonSubstring(self, A, B):
        # write your code here
        if not A or not B:
            return 0

        dp_table = [[0] * (len(B)+1) for _ in range(len(A) + 1)]

        max_len = 0

        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i-1] == B[j-1]:
                    dp_table[i][j] = dp_table[i - 1][j - 1] + 1
                else:
                    dp_table[i][j] = 0
                max_len = max(max_len, dp_table[i][j])

        return max_len