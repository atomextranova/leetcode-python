class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """

    def maxAverage(self, nums, k):
        # write your code here
        if not nums:
            return 0
        start, end = min(nums), max(nums)
        # binary search for possible answer
        while start + 1e-5 < end:
            mid = (start + end) / 2
            if self.can_find_larger_mean(nums, mid, k):
                start = mid
            else:
                end = mid

        return start

    def can_find_larger_mean(self, nums, target_average, k):
        # Construct prefix sum with average deducted
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num - target_average)

        min_prefix_sum = 0
        for i in range(k, len(nums) + 1):
            # if > 0, => prefix_sum > average
            if prefix_sum[i] - min_prefix_sum >= 0:
                return True
            min_prefix_sum = min(min_prefix_sum, prefix_sum[i - k + 1])

        return False