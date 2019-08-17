import sys

class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset
    """

    # Edge case:
    # empty set
    # same element
    # negative?
    # unordered: sort first

    # DP
    # State: dp_table[i]
    # Largest divisible set at index i given that max(set) = nums[i]
    # Function: dp_table[i] = dp_table[j] + 1 if nums[i] % nums[j] == 0 for all
    # j < i else 1 (this guarantees all nums % num == 0 for all num < nums[i-1]
    # in the set)
    # Initialization: all = 1
    # Answer: max(dp_table)

    def largestDivisibleSubset(self, nums):
        # write your code here

        if not nums:
            return 0

        length = len(nums)
        # sort first
        nums.sort()

        dp_table = [1] * length
        prev_list = [-1] * length

        for i in range(length):
            for j in range(i):
                if nums[i] % nums[j] != 0:
                    continue
                if dp_table[i] < dp_table[j] + 1:
                    dp_table[i] = dp_table[j] + 1
                    prev_list[i] = j

        max_val = -sys.maxsize - 1
        max_index = 0

        for i, val in enumerate(dp_table):
            if val > max_val:
                max_val = val
                max_index = i

        sequence_index = max_index
        result_list = []
        while sequence_index != -1:
            result_list.append(nums[sequence_index])
            sequence_index = prev_list[sequence_index]

        return result_list[::-1]