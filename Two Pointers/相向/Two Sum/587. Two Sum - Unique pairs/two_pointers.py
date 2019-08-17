class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """

    def twoSum6(self, nums, target):
        # write your code here
        nums.sort()
        if not nums:
            return -0

        left = 0
        right = len(nums) - 1
        count = 0
        while left < right:
            left_val = nums[left]
            right_val = nums[right]

            if left_val + right_val < target:
                left += 1
            elif left_val + right_val > target:
                right -= 1
            else:
                count += 1
                left += 1
                right -= 1

                while nums[left] == left_val and left < right:
                    left += 1
                while nums[right] == right_val and left < right:
                    right -= 1

        return count