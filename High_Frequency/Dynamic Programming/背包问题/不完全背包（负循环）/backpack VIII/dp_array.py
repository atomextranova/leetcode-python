class Solution:
    """
    @param n: the value from 1 - n
    @param value: the value of coins
    @param amount: the number of coins
    @return: how many different value
    """
    def backPackVIII(self, n, values, amount):
        # write your code here
        if n == 0 or not values or not amount:
            return 0

        dp = [False] * (n + 1)

        new_values = []

        for val, a in zip(values, amount):
            base = 1
            while base <= a:
                new_values.append(base * val)
                a -= base
                base *= 2

            if a > 0:
                new_values.append(a * val)

        dp[0] = True
        for i in range(len(new_values)):
            cur_val = new_values[i]
            for j in range(n, cur_val - 1, -1):
                dp[j] = dp[j] or dp[j - cur_val]

        return sum(dp) - 1