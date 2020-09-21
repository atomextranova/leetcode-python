from typing import List

DX = (1, -1, 0, 0)
DY = (0, 0, 1, -1)


class Solution:
    # Iterate
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        row_num = len(grid)
        col_num = len(grid[0])
        self.visited = set()
        self.unique_island = set()

        for x in range(row_num):
            for y in range(col_num):
                # index = self.position_to_index(x, y, col_num)
                if (x, y) in self.visited or grid[x][y] == 0:
                    continue
                to_be_visited = [(x, y)]
                # print(x, y)
                self.visited.add((x, y))
                cur_island = "00"
                while to_be_visited:
                    old_x, old_y = to_be_visited.pop()
                    # cur_island.append(old_relative_index)
                    for dx, dy in zip(DX, DY):
                        new_x = old_x + dx
                        new_y = old_y + dy
                        if not self.check_valid(new_x, new_y, row_num, col_num,
                                                grid):
                            continue
                        if (new_x, new_y) in self.visited:
                            continue
                        relative_x = new_x - x
                        relative_y = new_y - y
                        # Wrong to use index:
                        # special case exists
                        # [[1,1,1,1],[1,0,1,0],[0,0,0,0],[0,1,1,1],[1,1,0,1]]
                        # new_relative_index = self.position_to_index(
                        # relative_x,
                        #                                             relative_y,
                        #                                             col_num)
                        cur_island += str(relative_x) + str(relative_y)
                        to_be_visited.append((new_x, new_y))
                        self.visited.add((new_x, new_y))
                # shape_str = ",".join(cur_island)
                # print(self.visited)
                # print(cur_island)
                if cur_island in self.unique_island:
                    continue
                # print(cur_island)
                self.unique_island.add(cur_island)

        return len(self.unique_island)

    # Wrong to use
    # def position_to_index(self, x, y, col_num):
    #     return str(x * col_num + y)

    def check_valid(self, x, y, row_num, col_len, grid):
        return 0 <= x < row_num and 0 <= y < col_len and grid[x][y] == 1