import collections

DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class Solution:
    """
    @param arr: the map
    @return:  the smallest target that satisfies from the upper left corner (0, 0) to the lower right corner (n-1, n-1)
    """

    def mapJump(self, arr):
        # Write your code here.
        self.length = len(arr)
        if self.length == 1:
            return 0

        min_height = min(min(arr))
        max_height = max(max(arr))

        while min_height + 1 < max_height:
            mid_height = (max_height + min_height) // 2
            if self.bfs(arr, mid_height):
                max_height = mid_height
            else:
                min_height = mid_height

        if self.bfs(arr, min_height):
            return min_height
        else:
            return max_height

    def bfs(self, grid, target):
        deque = collections.deque([(0, 0)])
        visited = set()
        visited.add((0, 0))
        while deque:
            x, y = deque.popleft()

            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if self.is_valid(grid, new_x, new_y, target, visited):
                    diff = abs(grid[new_x][new_y] - grid[x][y])
                    if diff > target:
                        continue
                    if new_x == self.length - 1 and new_y == self.length - 1:
                        return True
                    deque.append((new_x, new_y))
                    visited.add((new_x, new_y))

        return False

    def is_valid(self, grid, i, j, target, visited):
        return -1 < i < self.length and -1 < j < self.length and (
            i, j) not in visited