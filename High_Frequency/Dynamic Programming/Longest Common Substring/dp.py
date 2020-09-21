class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    # DP
    # State: dp[i][j] = longest common up to A[i] and B[j]
    # Inclusive -> use len(A) and len(B)
    # Initialization:
    # All dp[i][0] and dp[0][j] initialize to 0/1
    # Transition:

    # Result: max_val encountered
    def longestCommonSubstring(self, A, B):
        # write your code here
        if not A or not B:
            return 0

        dp_table = [[0] * len(B) for _ in range(len(A))]

        max_len = 0

        for i in range(len(A)):
            if A[i] == B[0]:
                dp_table[i][0] = 1
                max_len = 1

        for i in range(len(B)):
            if A[0] == B[i]:
                dp_table[0][i] = 1
                max_len = 1

        for i in range(1, len(A)):
            for j in range(1, len(B)):
                if A[i] == B[j]:
                    dp_table[i][j] = dp_table[i - 1][j - 1] + 1
                    max_len = max(max_len, dp_table[i][j])

        return max_len
