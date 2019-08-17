class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        # write your code here
        results = []
        temp_results = []
        self.dfs(sorted(nums), len(nums), 0, results, temp_results)
        return results

    def dfs(self, nums, length, start_index, results, temp_results):
        results.append(list(temp_results))

        for i in range(start_index, length):
            if i != 0 and nums[i] == nums[i - 1] and start_index < i:
                continue
            temp_results.append(nums[i])
            self.dfs(nums, length, i + 1, results, temp_results)
            temp_results.pop()