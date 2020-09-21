import collections

DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    """
    @param mazeMap: a 2D grid
    @return: return the minium distance
    """

    def getMinDistance(self, mazeMap):
        # write your code here
        if not mazeMap or not mazeMap[0]:
            return -1

        col_len = len(mazeMap)
        row_len = len(mazeMap[0])
        start = (0, 0)
        end = (0, 0)
        jump_table = {}

        for i in range(col_len):
            for j in range(row_len):
                num = mazeMap[i][j]
                if num <= 0:
                    if num == -2:
                        start = (i, j)
                    elif num == -3:
                        end = (i, j)
                    continue
                if num not in jump_table:
                    jump_table[num] = [0, []]

                jump_table[num][1].append((i, j))

        visited = set()
        deque = collections.deque([start])
        visited.add(start)
        cost = 0

        while deque:
            for i in range(len(deque)):
                pos = deque.popleft()

                x, y = pos
                if pos == end:
                    return cost
                num = mazeMap[x][y]

                if num > 0 and jump_table[num][0] != 1:
                    jump_table[num][0] = 1
                    for new_pos in jump_table[num][1]:
                        if new_pos in visited:
                            continue
                        visited.add(new_pos)
                        deque.append(new_pos)

                for dx, dy in DIR:
                    new_x, new_y = x + dx, y + dy
                    new_pos = (new_x, new_y)
                    if not self.is_valid(new_x, new_y, col_len, row_len,
                                         visited, mazeMap):
                        continue
                    visited.add(new_pos)
                    deque.append(new_pos)
            cost += 1

        return -1

    def is_valid(self, x, y, col_len, row_len, visited, mazeMap):
        return -1 < x < col_len and -1 < y < row_len and (
        x, y) not in visited and mazeMap[x][y] != -1
