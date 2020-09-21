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
            base = 1
            while base <= amount:
                new_weights.append(weight[i] * base)
                new_prices.append(base * prices[i])
                amount -= base
                base *= 2

            if amount > 0:
                new_weights.append(weight[i] * amount)
                new_prices.append(amount * prices[i])

        dp = [0] * (n + 1)

        for i in range(len(new_prices)):
            for price in range(n, new_prices[i] - 1, -1):
                dp[price] = max(dp[price], dp[price - new_prices[i]] + new_weights[i])

        return dp[-1]
