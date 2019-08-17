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
        # Ordered
        candidates.sort()
        self.dfs(results, temp_results, candidates, target, 0, 0,
                 len(candidates))
        return results

    def dfs(self, results, temp_results, candidates, target, start_index
            , current_sum, length):
        if current_sum == target:
            results.append(list(temp_results))
            return

        if current_sum > target:
            return

        last_used = None
        for i in range(start_index, length):
            temp = candidates[i]
            # Duplicate
            if temp == last_used:
                continue
            last_used = temp
            temp_results.append(temp)
            self.dfs(results, temp_results, candidates, target, i
                     , current_sum + temp, length)
            temp_results.pop()