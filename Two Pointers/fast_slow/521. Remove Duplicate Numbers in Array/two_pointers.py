class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0

        slow = 0
        fast = 0
        count = 1

        nums.sort()

        while fast < len(nums):
            while fast < len(nums) and nums[slow] == nums[fast]:
                fast += 1
            if fast < len(nums):
                nums[count] = nums[fast]
                slow = count
                fast += 1
                count += 1

        return count
