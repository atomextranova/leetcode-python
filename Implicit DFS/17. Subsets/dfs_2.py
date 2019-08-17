class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        # write your code here
        results = []
        sorted_nums = sorted(nums)
        self.dfs(sorted_nums, results, 0, [], len(nums))
        return results

    def dfs(self, nums, results, start_index, temp_results, length):
        results.append(list(temp_results))

        for i in range(start_index, length):
            temp_results.append(nums[i])
            self.dfs(nums, results, i + 1, temp_results, length)
            temp_results.pop()