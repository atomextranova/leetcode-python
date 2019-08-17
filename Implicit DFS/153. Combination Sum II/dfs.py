class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
                # write your code here
        results = []
        temp_results = []
        # Ordered
        num.sort()
        self.dfs(results, temp_results, num, target, 0, 0,
                 len(num))
        return results

    def dfs(self, results, temp_results, candidates, target, start_index
            , current_sum, length):

        # Could be moved inside the loop. If so, add pop before return
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
            self.dfs(results, temp_results, candidates, target, i + 1,
            current_sum + temp, length)
            temp_results.pop()


sol = Solution()
print(sol.combinationSum2([7,1,2,5,1,6,10], 8))