class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        if nums is None:
            return []

        if len(nums) == 0:
            return [[]]

        results = []
        temp_results = []
        length = len(nums)
        nums.sort()
        used_table = [False] * length
        self.dfs(nums, used_table, results, temp_results, length)
        return results

    def dfs(self, nums, used_table, results, temp_results, length):
        if len(temp_results) == length:
            results.append(list(temp_results))
            return

        for i in range(length):
            if used_table[i]:
                continue

            used_table[i] = True
            temp_results.append(nums[i])
            self.dfs(nums, used_table, results, temp_results, length)
            used_table[i] = False
            temp_results.pop()