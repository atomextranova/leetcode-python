DX = (2, 1, -2, -1, 2, 1, -2, -1)
DY = (1, 2, -1, -2, -1, -2, 1, 2)


class Solution:
    # Optimization
    # Could use 2 dp_table here to track t-1 and t
    # Could use a dict to store visited map


    # State: dp[x][y][t] stands for the probability of arriving at x,y at time t
    # Initial state: dp_state[r][c][0] = 1
    # Transition: For each x,y, if dp_state[x][y][t-1] != 0
    # Then dp_table[new_x][new_y][t] += dp_state[x][y][t-1] / 8
    # Answer: sum of values in dp[x][y][K
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if N == 0:
            return 0

        if K == 0:
            return 1

        dp_table = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
        dp_table[r][c][0] = 1
        # Could also do bfs here, faster
        for i in range(1, K + 1):
            for x in range(N):
                for y in range(N):
                    print(x, y, i)
                    if dp_table[x][y][i - 1] == 0:
                        continue
                    for dx, dy in zip(DX, DY):
                        new_x = x + dx
                        new_y = y + dy
                        if not self.valid_position(new_x, new_y, N):
                            continue
                        dp_table[new_x][new_y][i] += dp_table[x][y][i - 1] / 8

        # print(dp_table)
        result = 0
        for x in range(N):
            for y in range(N):
                result += dp_table[x][y][K]
        return result

    def valid_position(self, r, c, N):
        return 0 <= r < N and 0 <= c < N


sol = Solution()
print(sol.knightProbability(3, 2, 0, 0))

