class Solution:
    """
    @param n: the number of tasks
    @param weights: the weight for every task
    @param tasks: the actual duration of every task
    @param p: maximum runtime for Pigeon in an hour
    @return: the maximum total weight that the Pigeon service can achieve in an hour
    """
    def maxWeight(self, n, weights, tasks, p):
        # write your code here
        dp = [0] * (p // 2 + 1)

        for i in range(n):
            for j in range(p // 2, tasks[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - tasks[i]] + weights[i])
            print(dp)

        return dp[-1]