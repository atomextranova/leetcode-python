class Solution:

    def prefix_sum_fair_index_count(self, A, B):
        fair_indexes_A = self.get_fair_indexes(A)
        if not fair_indexes_A:
            return 0
        fair_indexes_B = self.get_fair_indexes(B)
        if not fair_indexes_B:
            return 0
        return len(set(fair_indexes_A).intersection(set(fair_indexes_B)))

    def get_fair_indexes(self,nums):
        cur_sum = 0
        sum_to_indexes = {}
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum not in sum_to_indexes:
                sum_to_indexes[cur_sum] = []
            sum_to_indexes[cur_sum].append(i)

        if cur_sum / 2 not in sum_to_indexes:
            return None
        else:
            return sum_to_indexes[cur_sum / 2]

