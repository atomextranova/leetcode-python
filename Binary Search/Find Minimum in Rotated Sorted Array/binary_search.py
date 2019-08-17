class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums):
        # write your code here
        start = 0
        end = len(nums) - 1
        target = nums[end]

        while start + 1 < end:
            mid = start + ((end - start) >> 1)
            # Compare with nums[end] also works
            if nums[mid] < target:
                end = mid
            if nums[mid] > target:
                start = mid
            # start/end both works since no duplicates
            if nums[mid] == target:
                end = mid

        return min(nums[start], nums[end])