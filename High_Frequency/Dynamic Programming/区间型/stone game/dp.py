class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        if len(A) <= 1:
            return 0

        prefix_sums = [0] * (len(A) + 1)

        index = 1
        cur_sum = 0
        for a in A:
            cur_sum += a
            prefix_sums[index] = cur_sum
            index += 1
        print(prefix_sums)
        dp = [[0] * len(A) for _ in range(len(A))]

        for length in range(2, len(A) + 1):
            for left in range(len(A) + 1 - length):
                right = left + length - 1
                dp[left][right] = float('inf')
                for mid in range(left, right):
                    dp[left][right] = min(dp[left][right], dp[left][mid] + dp[mid+1][right] + prefix_sums[right+1] - prefix_sums[left])

        return dp[0][-1]