class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        if not nums:
            return -1

        if s == 0:
            return 0

        cur_sum = 0
        right = 0
        min_length = float('inf')
        for left in range(len(nums)):
            while right < len(nums) and cur_sum < s:
                cur_sum += nums[right]
                right += 1

            if cur_sum >= s:
                min_length = min(min_length, right - left)

            cur_sum -= nums[left]

        return min_length if min_length != float('inf') else -1