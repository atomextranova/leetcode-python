def matrixRestoration(self, n, m, after):
    # 倒序遍历矩阵
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            # 减去上面的部分
            if i > 0:
                after[i][j] -= after[i - 1][j]
            # 减去左面的部分
            if j > 0:
                after[i][j] -= after[i][j - 1]
            # 加上重复减去的部分
            if i > 0 and j > 0:
                after[i][j] += after[i - 1][j - 1]

    return after