import collections
import copy
DIR = [[0, 1], [1, 0], [-1, 0], [0, -1]]

class Solution:
    """
    @param board: the given board
    @return:  the least number of moves required so that the state of the board is solved
    """

    # Can be optimized by change a board to string
    def slidingPuzzle(self, board):
        # write your code here

        visited = set()
        deque = collections.deque([([[1, 2, 3], [4, 5, 0]], (1, 2))])
        visited.add(((1, 2, 3), (4, 5, 0)))
        distance = 0
        while deque:
            for _ in range(len(deque)):
                cur, index = deque.popleft()
                if self.reach(cur, board):
                    return distance

                x, y = index
                for dx, dy in DIR:
                    next_x = x + dx
                    next_y = y + dy
                    if not self.is_valid(next_x, next_y):
                        continue
                    new_board = copy.deepcopy(cur)
                    new_board[next_x][next_y], new_board[x][y] = new_board[x][y], new_board[next_x][next_y]
                    record = tuple(tuple(sub) for sub in new_board)
                    if record in visited:
                        continue
                    visited.add(record)
                    deque.append((new_board, (next_x, next_y)))
            distance += 1
        return -1

    def reach(self, cur, target):
        for i in range(2):
            for j in range(3):
                if cur[i][j] != target[i][j]:
                    return False

        return True

    def is_valid(self, x, y):
        return -1 < x < 2 and -1 < y < 3
