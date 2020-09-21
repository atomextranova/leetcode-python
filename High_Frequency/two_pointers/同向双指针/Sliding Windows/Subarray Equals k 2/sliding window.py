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
        max_len = float('inf')

        cur_sum = 0
        prefix_sums = []
        target_sums = defaultdict(set)
        target_sums[0].add(-1)
        for i, num in enumerate(nums):
            cur_sum += num
            prefix_sums.append(cur_sum)
            target_sums[cur_sum].add(i)
        print(target_sums)
        print(target_sums[3])
        for i, prefix_sum in enumerate(prefix_sums):
            diff = k - prefix_sum
            left_index = -1
            print(target_sums[diff])
            for index in target_sums[diff]:
                print(index)
                if left_index < index < i:
                    left_index = index
            print(prefix_sum, diff, i, left_index)
            max_len = min(max_len, i - left_index + 1)

        return max_len

sol = Solution()
sol.subarraySumEqualsKII([2,1,-1,4,2,-3], 3)