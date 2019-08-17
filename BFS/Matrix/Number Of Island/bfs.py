DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here

        self.row_length = len(grid)
        if self.row_length == 0:
            return 0
        self.column_length = len(grid[0])
        if self.column_length == 0:
            return 0

        visited_dict = set()

        count = 0
        for row_index in range(self.row_length):
            for column_index in range(self.column_length):
                next_pos = (row_index, column_index)
                if next_pos in visited_dict:
                    continue
                if grid[row_index][column_index]:
                    visited_dict.add(next_pos)
                    self.bfs(grid, row_index, column_index, visited_dict)
                    count += 1
        return count

    def bfs(self, grid, row_index_orig, column_index_orig, visited_dict):
        to_be_visted = [(row_index_orig, column_index_orig)]

        while to_be_visted:
            row_index, column_index = to_be_visted.pop(0)
            for row_offset, column_offset in DIRECTION:
                row_next = row_index + row_offset
                column_next = column_index + column_offset
                if (row_next, column_next) in visited_dict:
                    continue
                if self.is_valid(row_next, column_next):
                    if grid[row_next][column_next]:
                        visited_dict.add((row_next, column_next))
                        to_be_visted.append((row_next, column_next))

    def is_valid(self, row_index, column_index):
        return 0 <= row_index < self.row_length and 0 <= column_index < self.column_length


inputs = []
sol =Solution()
print(sol.numIslands(inputs))
print()