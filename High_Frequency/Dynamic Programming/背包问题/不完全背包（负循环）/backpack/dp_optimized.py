class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        if not m or not A:
            return 0

        dp = [[False] * (m + 1) for _ in range(2)]

        dp[0][0] = True
        for i in range(1, len(A) + 1):
            index = i % 2
            dp[index][0] = True
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    dp[index][j] = dp[index - 1][j] or dp[index - 1][j - A[i - 1]]
                else:
                    dp[index][j] = dp[index - 1][j]
            # dp[index-1] = [False] * (m + 1)
        for j in range(m, -1, -1):
            if dp[i % 2][j]:
                return j
        return 0