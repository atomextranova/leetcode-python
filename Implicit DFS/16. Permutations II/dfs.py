class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
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
            # Append to store reachable solution
            results.append(list(temp_results))
            return
        last_val = None
        for i in range(length):
            if used_table[i]:
                continue
            # Or if (i > 0 and nums[i] == nums[i - 1] and not used_table[i - 1])
            if nums[i] == last_val:
                continue

            used_table[i] = True
            temp_results.append(nums[i])
            self.dfs(nums, used_table, results, temp_results, length)
            used_table[i] = False
            temp_results.pop()
            last_val = nums[i]