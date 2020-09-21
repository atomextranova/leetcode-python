import collections

DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class Solution:
    """
    @param grid: a 2d boolean array
    @param k: an integer
    @return: the number of Islands
    """

    def numsofIsland(self, grid, k):
        # Write your code here
        if not grid or not grid[0]:
            return 0
        self.col_len = len(grid)
        self.row_len = len(grid[0])
        self.visited = set()

        result = 0
        for i in range(self.col_len):
            for j in range(self.row_len):
                if self.is_valid(grid, i, j):
                    island_size = self.bfs(grid, i, j)
                    if island_size >= k:
                        result += 1

        return result

    def bfs(self, grid, i, j):
        deque = collections.deque([(i, j)])
        self.visited.add((i, j))
        size = 0
        cur = []
        while deque:
            x, y = deque.popleft()
            cur.append((x, y))
            size += 1
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if self.is_valid(grid, new_x, new_y):
                    deque.append((new_x, new_y))
                    self.visited.add((new_x, new_y))
        return size

    def is_valid(self, grid, i, j):
        return -1 < i < self.col_len and -1 < j < self.row_len and (
        i, j) not in self.visited and grid[i][j] == 1
    
sol = Solution()
sol.numsofIsland([[1,1,0,1,0],[0,0,0,1,1],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,1]], 5)