import sys

class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """

    # Edge case:
    # empty
    # last element is s

    # Two pointers

    # O(n), worst case 2n

    def minimumSize(self, nums, s):
        # write your code here
        if not nums:
            return -1

        slow = 0
        fast = 0

        length = len(nums)
        current_sum = 0
        min_length = sys.maxsize

        for fast in range(length):
            current_sum += nums[fast]

            if current_sum < s:
                continue

            while current_sum - nums[slow] >= s:
                current_sum -= nums[slow]
                slow += 1

            min_length = min(min_length, fast - slow + 1)

        if min_length == sys.maxsize:
            return -1

        return min_length
