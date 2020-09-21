from collections import deque

DIRECTIONS = [
    (1, 0),
    (0, -1),
    (-1, 0),
    (0, 1),
]


class Solution:
    """
    @param targetMap:
    @return: nothing
    """
    # Standard Bi-BFS
    # 1. Create visited(set), start_deque(deque) and end_deque
    # 2. Do one step for start_deque and one for end_deque
    # a. for each step, do a step of standard bfs by layer
    # b. visited record 1 for one direction, -1 for one direction
    # c. once a grid is known to have both 1 and -1, the result is found
    # 3. return -1 if not found
    def shortestPath(self, targetMap):
        # Write your code here
        if not targetMap or not targetMap[0]:
            return -1

        self.x_max = len(targetMap)
        self.y_max = len(targetMap[0])
        tx, ty = self.find_target(targetMap)
        if (tx, ty) == (-1, -1):
            return -1

        if (tx, ty) == (0, 0):
            return 0

        visited = [[0] * self.y_max for _ in range(self.x_max)]
        visited[0][0] = 1
        visited[tx][ty] = -1
        forward = deque([(0, 0)])
        backward = deque([(tx, ty)])
        step = 0

        while forward and backward:
            if self.find_next_step(forward, visited, targetMap, 1):
                return step
            step += 1

            if self.find_next_step(backward, visited, targetMap, -1):
                return step
            step += 1

        return -1

    def find_target(self, targetMap):
        for i in range(len(targetMap)):
            for j in range(len(targetMap[0])):
                if targetMap[i][j] == 2:
                    return (i, j)

        return -1, -1

    def check_valid(self, x, y, targetMap, visited, mark):
        return -1 < x < self.x_max and -1 < y < self.y_max and targetMap[x][
            y] != 1 and visited[x][y] != mark

    def find_next_step(self, to_be_visited, visited, targetMap, mark):
        for i in range(len(to_be_visited)):
            cur_x, cur_y = to_be_visited.popleft()

            for x, y in DIRECTIONS:
                next_x, next_y = (cur_x + x, cur_y + y)
                if not self.check_valid(next_x, next_y, targetMap, visited,
                                        mark):
                    continue
                if visited[cur_x][cur_y] + mark == 0:
                    return True

                to_be_visited.append((next_x, next_y))
                visited[next_x][next_y] = mark

        return False

sol = Solution()
targetMap = [
 [0, 0, 0],
 [0, 0, 2]
]
print(sol.shortestPath(targetMap))