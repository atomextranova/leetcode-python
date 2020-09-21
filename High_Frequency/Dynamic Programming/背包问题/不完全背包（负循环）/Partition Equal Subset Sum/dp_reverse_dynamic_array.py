class Solution:
    """
    @param nums: a non-empty array only positive integers
    @return: true if can partition or false
    """
    def canPartition(self, nums):
        # sum用来记录总和
        sum = 0
        for x in nums:
            sum += x
        if sum % 2 == 1:
            return False
        capacity = sum // 2
        # dp[i]表示是否有这样一种可行方案使得元素和为i
        dp = [False] * (capacity + 1)
        dp[0] = True
        for i in range(len(nums)):
            for j in range(capacity, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]

        return dp[capacity]