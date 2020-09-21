import collections

class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        # write your code here
        if not nums or k > len(nums):
            return 0

        val = 1e-5

        left = min(nums)
        right = max(nums)

        while left + val < right:
            mid = (left + right) / 2

            if self.valid(mid, nums, k):
                left = mid
            else:
                right = mid

        if self.valid(left, nums, k):
            return left
        else:
            return right

    def valid(self, val, nums, k):
        new_nums = [0] * (len(nums) + 1)
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i] - val
            new_nums[i+1] = cur_sum
        min_prefix_sum = 0
        for i in range(k, len(nums) + 1):
            if new_nums[i] - min_prefix_sum >= 0:
                return True
            min_prefix_sum = min(min_prefix_sum, new_nums[i-k+1])

        return False