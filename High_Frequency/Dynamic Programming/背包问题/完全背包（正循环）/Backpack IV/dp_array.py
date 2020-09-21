class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackIV(self, nums, target):
        # write your code here
        length = target + 1
        dp = [0] * length
        dp[0] = 1
        for num in nums:
            for j in range(num, length):
                dp[j] += dp[j - num]

        return dp[-1]