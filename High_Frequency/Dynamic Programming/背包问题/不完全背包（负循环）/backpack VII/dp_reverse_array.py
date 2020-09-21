class Solution:
    """
    @param n: the money of you
    @param prices: the price of rice[i]
    @param weight: the weight of rice[i]
    @param amounts: the amount of rice[i]
    @return: the maximum weight
    """
    def backPackVII(self, n, prices, weight, amounts):
        # write your code here
        if n == 0 or not prices or not weight or not amounts:
            return 0

        new_prices = []
        new_weights = []

        for i in range(len(amounts)):
            amount = amounts[i]
            for _ in range(amount):
                new_weights.append(weight[i])
                new_prices.append(prices[i])

        dp = [0] * (n + 1)

        for i in range(len(new_prices)):
            for price in range(n, new_prices[i] - 1, -1):
                dp[price] = max(dp[price], dp[price - new_prices[i]] + new_weights[i])

        return dp[-1]
