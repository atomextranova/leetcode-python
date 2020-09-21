from collections import defaultdict


class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
    """

    def subarraySumEqualsKII(self, nums, k):
        # write your code here
        left = 0
        right = 0
        max_len = len(nums) + 1

        cur_sum = 0
        prefix_sums = []
        target_sums = defaultdict(int)
        target_sums[0] = -1
        for i, num in enumerate(nums):
            cur_sum += num
            prefix_sums.append(cur_sum)

            diff = cur_sum - k
            if diff in target_sums:
                max_len = min(max_len, i - target_sums[diff])

            target_sums[cur_sum] = i

        return max_len
