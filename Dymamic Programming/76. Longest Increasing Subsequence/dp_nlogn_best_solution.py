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
    # duplicates?

    # dp
    # state: dp_table[i] LIS from 0 to i given that nums[i] is the end !!!
    # fucntion: dp_table[i] = max(dp_table[i], dp_table[x] + 1) if nums[i] > nums[x]
    # initialization: dp_table[all] = 1 !!!
    # answer: max(dp_table)

    # print: the longest sequence, if multiple, will print the one with every
    # element smallest
    # return: length

    # time: O(nlongn)

    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0

        length = len(nums)
        dp_table = [1] * length
        # make sure index == length of sequence
        # element of index i -> the smallest end number of sequence of length i
        # length + 1 to make sure binary search works and index == length
        min_last = [(sys.maxsize, -1)] * (length + 1)
        min_last[0] = (-sys.maxsize - 1, -1)

        prev_list = [-1] * length
        longest = 1

        for i in range(0, length):
            index = self.binary_search(min_last, nums[i])
            # update prev info
            if index > 1:
                prev_list[i] = min_last[index-1][1]
            min_last[index] = (nums[i], i)

            if index > longest:
                longest = index

        result = []
        last_element, last_element_index = min_last[longest]
        result.append(last_element)
        prev_index = prev_list[last_element_index]
        while prev_index != -1:
            result.append(nums[prev_index])
            prev_index = prev_list[prev_index]

        print(result)

        # for i in range(length - 1, 0, -1):
        #     if (min_last[i] != sys.maxsize):
        #         return i

        # return 0
        return longest

    # Index of first number > val
    def binary_search(self, min_last, val):
        start = 0
        end = len(min_last) - 1

        while start + 1 < end:
            mid = (end - start) // 2 + start
            if min_last[mid][0] < val:
                start = mid
            else:
                end = mid

        return end

sol = Solution()
sol.longestIncreasingSubsequence([4,2,4,5,3,7])