from typing import List


class Solution:
    # prefix sum
    # O(n^2)
    # O(n) space
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        prefix_sums = [0] * len(nums)
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num
            prefix_sums[i] = cur_sum

        count = 0
        for i in range(len(nums)):
            prefix = prefix_sums[i]
            if prefix == k:
                count += 1
            for j in range(i):
                if prefix - prefix_sums[j] == k:
                    count += 1

        return count