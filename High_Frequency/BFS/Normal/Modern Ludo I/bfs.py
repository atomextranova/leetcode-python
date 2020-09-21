import collections

class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """
    def modernLudo(self, length, connections):
        # Write your code here
        connect = {}
        for connection in connections:
            x, y = connection
            connect[x] = y

        if length == 1:
            return 0

        deque = collections.deque([(1, 0)])
        visited = {}
        while deque:
            for i in range(len(deque)):
                x, dist = deque.popleft()
                temp_x = x
                if temp_x == length:
                    return dist

                while temp_x in connect:
                    temp_x = connect[temp_x]
                    if temp_x in visited:
                        if visited[temp_x] > dist:
                            visited[temp_x] = dist
                        else:
                            break

                    deque.appendleft((temp_x, dist))
                    visited[temp_x] = dist

                for j in range(1, 7):
                    new_x = x + j
                    if new_x in visited or new_x >= length + 1:
                        continue
                    visited[new_x] = dist + 1
                    deque.append((new_x, dist + 1))

        return -1