class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        prefix_sum = 0
        for i, x in enumerate(nums):
            if prefix_sum == (S - prefix_sum - x):
                return i
            prefix_sum += x
        return -1