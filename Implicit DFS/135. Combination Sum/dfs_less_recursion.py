class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates, target):
        # write your code here
        results = []
        temp_results = []
        candidates.sort()
        self.dfs(results, temp_results, candidates, target, 0, 0,
                 len(candidates))
        return results

    def dfs(self, results, temp_results, candidates, target, start_index
            , current_sum, length):

        last_used = None
        for i in range(start_index, length):
            temp = candidates[i]
            if temp == last_used:
                continue
            last_used = temp
            temp_sum = temp + current_sum
            temp_results.append(temp)
            if temp_sum == target:
                results.append(list(temp_results))
                temp_results.pop()
                return

            if temp_sum > target:
                temp_results.pop()
                return

            self.dfs(results, temp_results, candidates, target, i
                     , temp_sum, length)
            temp_results.pop()