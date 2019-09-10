from collections import defaultdict


class Solution:
    # O(n) time
    # O(n) space
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        cur_sum = 0
        count = 0
        # or counter.count(nums)
        sum_to_count = defaultdict(int)
        sum_to_count[0] = 1
        for num in nums:
            cur_sum += num
            count += sum_to_count[cur_sum - k]
            sum_to_count[cur_sum] += 1

        return count