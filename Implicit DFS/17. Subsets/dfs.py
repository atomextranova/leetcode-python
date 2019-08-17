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
        if start_index == length:
            results.append(list(temp_results))
            return

        temp_results.append(nums[start_index])
        self.dfs(nums, results, start_index + 1, temp_results, length)
        temp_results.pop()
        self.dfs(nums, results, start_index + 1, temp_results, length)

sol = Solution()
sol.subsets([1, 2, 3])