

def max_min_path(matrix):
    if not matrix or not matrix[0]:
        return 0

    n, m = len(matrix), len(matrix[0])

    if n * m <= 2:
        return 0

    dp = [[0] * m for _ in range(n)]
    dp[0][1] = matrix[0][1]
    dp[1][0] = matrix[1][0]
    for i in range(2, m):
        dp[0][i] = min(matrix[0][i], dp[0][i-1])

    for i in range(2, n):
        dp[i][0] = min(matrix[i][0], dp[i-1][0])

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(matrix[i][j], max(dp[i - 1][j], dp[i][j - 1]))

    if n == 1:
        return dp[0][-2]
    elif m == 1:
        return dp[-2][0]
    else:
        return max(dp[-2][-1], dp[-1][-2])

case = [[5, 1],
 [4, 5]]
print(max_min_path(case))
case = [[1, 2, 3], [4, 5, 1]]
print(max_min_path(case))