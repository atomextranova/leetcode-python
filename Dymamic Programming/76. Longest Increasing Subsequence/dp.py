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
    # fucntion: dp_table[i] = max(dp_table[i], dp_table[x] + 1)
    # if nums[i] > nums[x]
    # initialization: dp_table[all] = 1 !!!
    # answer: max(dp_table)

    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0

        length = len(nums)
        dp_table = [1] * length

        for i in range(1, length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp_table[i] = max(dp_table[i], dp_table[j] + 1)
        return max(dp_table)
