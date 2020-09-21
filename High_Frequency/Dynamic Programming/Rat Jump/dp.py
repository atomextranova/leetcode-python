
class Solution:
    """
    @param arr: the steps whether have glue
    @return: the sum of the answers
    """

    def ratJump(self, arr):
        # Write your code here.

        MOD = 1e9 + 7
        new_arr = arr + [0, 0, 0]

        dp = [[0, 0] for _ in range(len(new_arr))]
        dp[0][0] = 1

        odd = [1, 2, 4]
        even = [1, 3, 4]


        for i in range(len(arr) - 1):
            for j in range(3):
                if new_arr[i] == 0:
                    dp[i+odd[j]][1] += dp[i][0]
                    dp[i+even[j]][0] += dp[i][1]
                    dp[i+odd[j]][1] %= MOD
                    dp[i+even[j]][0] %= MOD

        result = 0
        for i in range(-4, 0):
            result += sum(dp[i])
        return int(result % MOD)


        