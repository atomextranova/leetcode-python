import collections

DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """

    def shortestDistance(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return -1

        self.col_len = len(grid)
        self.row_len = len(grid[0])
        self.distance_map = [[0] * self.row_len for _ in range(self.col_len)]
        self.reachable_count = dict()
        room_count = 0
        for i in range(self.col_len):
            for j in range(self.row_len):
                if grid[i][j] != 1:
                    continue
                room_count += 1
                self.bfs(grid, i, j)

        min_distance = float('inf')
        for i, j in self.reachable_count:
            if self.reachable_count[(i, j)] != room_count or grid[i][j] == 1:
                continue
            min_distance = min(min_distance, self.distance_map[i][j])

        return min_distance if min_distance != float('inf') else -1

    def bfs(self, grid, x, y):
        deque = collections.deque([(x, y)])
        visited = set()
        visited.add((x, y))

        distance = 0
        while deque:
            for i in range(len(deque)):
                x, y = deque.popleft()
                self.reachable_count[(x, y)] = self.reachable_count.get((x, y),
                                                                        0) + 1
                self.distance_map[x][y] += distance

                for dx, dy in DIRECTIONS:
                    new_x, new_y = x + dx, y + dy
                    if not self.is_valid(grid, new_x, new_y, visited):
                        continue
                    deque.append((new_x, new_y))
                    visited.add((new_x, new_y))
            distance += 1

    def is_valid(self, grid, x, y, visited):
        return -1 < x < self.col_len and -1 < y < self.row_len and grid[x][
            y] == 0 and (x, y) not in visited

sol = Solution()
sol.shortestDistance([[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]])