import collections

DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]


class Solution:
    """
    @param side_length: the length of a side of the lake (it's a square)
    @param lake_grid: a 2D matrix representing the lake 0= ice, 1= snowbank, -1= hole
    @param albert_row: row of Albert's snowbank
    @param albert_column: column of Albert's snowbank
    @param kuna_row: row of Kuna's snowbank
    @param kuna_column: column of Kuna's snowbank
    @return: a bool - whether Albert can escape
    """

    def lakeEscape(self, side_length, lake_grid, albert_row, albert_column,
                   kuna_row, kuna_column):
        # write your code here

        explored = set()
        deque = collections.deque([(False, albert_row, albert_column)])

        while deque:
            found_kuna, x, y = deque.popleft()
            if (found_kuna, x, y) in explored:
                continue
            explored.add((found_kuna, x, y))
            for i in range(4):
                found_kuna_cur = False
                can_leave = False
                reach_bank = False
                dx, dy = DIR[i]
                new_x, new_y = x, y
                while True:
                    new_x, new_y = new_x + dx, new_y + dy
                    if not self.is_valid(side_length, new_x, new_y):
                        can_leave = True
                        break
                    if lake_grid[new_x][new_y] == 1:
                        if new_x == kuna_row and new_y == kuna_column:
                            found_kuna_cur = True
                        reach_bank = True
                        break
                    elif lake_grid[new_x][new_y] == -1:
                        break
                    else:
                        continue
                if can_leave and (found_kuna_cur or found_kuna):
                    return True
                elif reach_bank:
                    deque.append((found_kuna or found_kuna_cur, new_x, new_y))

        return False

    def is_valid(self, n, x, y):
        return -1 < x < n and -1 < y < n