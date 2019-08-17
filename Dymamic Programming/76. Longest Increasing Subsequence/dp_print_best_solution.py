class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    # input: array of interger
    # output: length of LIS
    # edge case:
    # nums = [], reutrn 0
    # duplicates?

    # dp
    # state: dp_table[i] LIS from 0 to i given that nums[i] is the end !!!
    # fucntion: dp_table[i] = max(dp_table[i], dp_table[x] + 1) if nums[i] > nums[x]
    # initialization: dp_table[all] = 1 !!!
    # answer: max(dp_table)

    # print: the longest sequence, if multiple, will print the one with every
    # element smallest
    # return: length

    # Time: O(n^2)

    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0

        length = len(nums)
        dp_table = [1] * length
        prev = [-1] * length

        for i in range(1, length):
            for j in range(i):
                # need to update prev and dp_table if dp_table < +1
                if nums[i] > nums[j] and dp_table[i] < dp_table[j] + 1:
                    dp_table[i] = dp_table[j] + 1
                    prev[i] = j
        # find the last element of the longest
        # use prev to print out the longest
        # [::-1] to reverse

        return max(dp_table)
