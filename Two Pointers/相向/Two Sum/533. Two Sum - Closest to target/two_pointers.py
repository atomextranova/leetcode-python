import sys

class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """

    def twoSumClosest(self, nums, target):
        # write your code here
        nums.sort()
        left = 0
        right = len(nums) - 1
        difference = sys.maxsize
        while left < right:
            temp_diff = nums[left] + nums[right] - target
            if temp_diff < 0:
                left += 1
            elif temp_diff > 0:
                right -= 1
            else:
                return 0
            difference = min(difference, abs(temp_diff))

        return difference