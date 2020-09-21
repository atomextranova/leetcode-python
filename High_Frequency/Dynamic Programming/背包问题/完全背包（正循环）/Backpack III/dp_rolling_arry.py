class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        # write your code here
        dp = [0] * (m + 1)

        modified = True
        for i in range(len(A)):
            cur_size = A[i]
            cur_val = V[i]
            # For dp[i][j], represents the max value can get with A[:i]
            # Since A[i] is unlimited, update from left to right to reflect.
            # Meaning in the same round, the A[i] can be taken
            # as many as the backpack can hold
            for size in range(cur_size, m + 1):
                dp[size] = max(dp[size], dp[size - cur_size] + cur_val)

        return dp[-1]

