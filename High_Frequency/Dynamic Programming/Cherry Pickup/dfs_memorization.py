class Solution:

    # DFS + Memorization
    # Problem formation
    # 2 paths both start from (0, 0) to (N-1, N-1)
    # find the total cherries
    # key: x, y: first path; x2, y2: 2nd path
    # total = max future cherries from x, y, x2, y2 to next positions +
    # current, consider if x == x2 and y == y2, avoid repetive adding
    # if not a valid index or
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        row_len = len(grid)
        memo = {}
        result = self.dfs_search(0, 0, 0, 0, row_len, grid, memo)
        return result if result > 0 else 0

    def dfs_search(self, x, y, x2, y2, N, grid, memo):
        if not self.valid_index(x, y, x2, y2, N):
            return float('-inf')

        if grid[x][y] == -1 or grid[x2][y2] == -1:
            return float('-inf')

        if x == N - 1 and y == N - 1:
            return grid[x][y] if grid[x][y] >= 0 else float('-inf')

        if (x, y, x2, y2) in memo:
            return memo[(x, y, x2, y2)]

        prev_max_val = max(self.dfs_search(x + 1, y, x2 + 1, y2, N, grid, memo),
                           self.dfs_search(x + 1, y, x2, y2 + 1, N, grid, memo),
                           self.dfs_search(x, y + 1, x2 + 1, y2, N, grid, memo),
                           self.dfs_search(x, y + 1, x2, y2 + 1, N, grid, memo))
        if prev_max_val == float('-inf'):
            memo[(x, y, x2, y2)] = float('-inf')

        if x == x2 and y == y2:
            max_val = prev_max_val + grid[x][y]
        else:
            max_val = prev_max_val + grid[x][y] + grid[x2][y2]

        memo[(x, y, x2, y2)] = max_val

        return memo[(x, y, x2, y2)]

    def valid_index(self, x, y, x2, y2, N):
        return 0 <= x < N and 0 <= y < N and 0 <= x2 < N and 0 <= y2 < N