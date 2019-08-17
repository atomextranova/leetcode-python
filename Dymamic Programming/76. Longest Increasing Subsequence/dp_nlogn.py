import sys

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    # input: array of interger
    # output: length of LIS
    # edge case:
    # nums = [], reutrn 0

    # dp
    # state: dp_table[i] LIS from 0 to i given that nums[i] is the end !!!
    # fucntion: dp_table[i] = max(dp_table[i], dp_table[x] + 1) if nums[i] > nums[x]
    # initialization: dp_table[all] = 1 !!!
    # answer: max(dp_table)

    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0

        length = len(nums)
        dp_table = [1] * length
        # make sure index == length of sequence
        # element of index i -> the smallest end number of sequence of length i
        min_last = [sys.maxsize] * (length + 1)
        min_last[0] = -sys.maxsize - 1

        prev_list = [-1] * length
        longest = 1

        for i in range(0, length):
            index = self.binary_search(min_last, nums[i])
            min_last[index] = nums[i]
            if index > longest:
                longest = index

        return longest

    # Index of first number > val
    def binary_search(self, min_last, val):
        start = 0
        end = len(min_last) - 1

        while start + 1 < end:
            mid = (end - start) // 2 + start
            if min_last[mid] < val:
                start = mid
            else:
                end = mid

        return end

sol = Solution()
sol.longestIncreasingSubsequence([4,2,4,5,3,7])