# https://leetcode.com/discuss/interview-question/383669/

def max_min_path(matrix):
    if not matrix or not matrix[0]:
        return 0

    n, m = len(matrix), len(matrix[0])

    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            elif i == 1 and j == 0 or i == 0 and j == 1:
                dp[i][j] = matrix[i][j]
            elif i == 0:
                dp[i][j] = min(matrix[i][j], matrix[i][j - 1])
            elif j == 0:
                dp[i][j] = min(matrix[i][j], matrix[i - 1][j])
            else:
                dp[i][j] = min(matrix[i][j], max(dp[i - 1][j], dp[i][j - 1]))

    if n == 1:
        return dp[0][-2]
    elif m == 1:
        return dp[-2][0]
    else:
        return max(dp[-2][-1], dp[-1][-2])

case = [[5],
 [5]]
print(max_min_path(case))