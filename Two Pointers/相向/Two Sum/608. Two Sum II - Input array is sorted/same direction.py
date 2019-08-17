class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + Triangle Count, index2 + Triangle Count] (index1 < index2)
    """

    def twoSum(self, nums, target):
        # write your code here
        if not nums:
            return -1, -1

        left = 0
        right = len(nums) - 1

        while left < right:
            left_val = nums[left]
            right_val = nums[right]

            if left_val + right_val < target:
                left += 1
            elif left_val + right_val > target:
                right -= 1
            else:
                return left + 1, right + 1

        return -1, -1