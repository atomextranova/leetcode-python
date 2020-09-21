class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # 如果背包容量或者物品数量为0，则直接返回
        if m == 0 or len(A) == 0:
            return 0

        dp = [0 for _ in range(m + 1)]
        for i in range(len(A)):
            # 滚动数组优化 倒序枚举j
            for j in range(m, A[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - A[i]] + A[i])

        return dp[m]