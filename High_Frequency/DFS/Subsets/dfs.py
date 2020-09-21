class Solution:
    # DFS
    # start from 0, two dfs call, one add element, one not
    # reach the end, append copy of current result
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        if nums:
            self.dfs(0, nums, [], result)

        return result

    def dfs(self, index, nums, temp_result, result):

        if index == len(nums):
            result.append(list(temp_result))
            return

        self.dfs(index + 1, nums, temp_result, result)
        temp_result.append(nums[index])
        self.dfs(index + 1, nums, temp_result, result)
        temp_result.pop()