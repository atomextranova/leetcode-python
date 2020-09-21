class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    def MinAdjustmentCost(self, A, target):
        # write your code here
        if target >= 100 or not A:
            return 0

        dp = [[float('inf')] * 101 for _ in range(len(A))]

        for i in range(101):
            dp[0][i] = abs(i - A[0])

        for i in range(1, len(A)):
            for target_val in range(101):
                min_val = max(0, target_val - target)
                max_val = min(101, target_val + target + 1)
                change = abs(A[i] - target_val)
                for cur_val in range(min_val, max_val):
                    dp[i][target_val] = min(dp[i][target_val],
                                            dp[i-1][cur_val] + change)

        return min(dp[-1])
    
sol = Solution()
sol.MinAdjustmentCost([1,4,2,3], 1)