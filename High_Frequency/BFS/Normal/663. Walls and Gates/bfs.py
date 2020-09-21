dx_list = [-1, 1, 0, 0]
dy_list = [0, 0, -1, 1]

from collections import deque


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    # Put all start on the queue
    # Try visiting all valid indexes
    # Edit distance
    def wallsAndGates(self, rooms):
        # write your code here
        if not rooms:
            return

        self.row_length = len(rooms)
        self.col_length = len(rooms[0])

        gates_list = deque()
        for i in range(self.row_length):
            for j in range(self.col_length):
                if rooms[i][j] != 0:
                    continue
                gates_list.append((i, j))

        while gates_list:
            for i in range(len(gates_list)):
                x, y = gates_list.popleft()
                for dx, dy in zip(dx_list, dy_list):
                    new_x = x + dx
                    new_y = y + dy
                    if not self.valid_next_step(new_x, new_y, rooms):
                        continue
                    gates_list.append((new_x, new_y))
                    rooms[new_x][new_y] = rooms[x][y] + 1

    def valid_next_step(self, i, j, rooms):
        return 0 <= i < self.row_length and 0 <= j < self.col_length and \
               rooms[i][j] == 2147483647