class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def moveZeroes(self, nums):
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                if slow != fast:
                    nums[slow] = nums[fast]
                slow += 1
            fast += 1

        while slow < len(nums):
            if nums[slow] != 0:
                nums[slow] = 0
            slow += 1