class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        n = len(costs)
        if n == 0:
            return 0
        dp = [[float('inf')] * 3 for _ in range(len(costs) + 1)]
        dp[0] = [0, 0, 0]
        for i in range(1, len(dp)):
            for j in range(3):
                for k in range(3):
                    if j == k:
                        continue
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + costs[i-1][j])

        return min(dp[-1])