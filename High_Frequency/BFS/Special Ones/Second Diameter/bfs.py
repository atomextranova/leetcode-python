import collections

class Solution:
    """
    @param edge: edge[i][0] [1] [2]  start point,end point,value
    @return: return the second diameter length of the tree
    """
    def getSecondDiameter(self, edges):
        # write your code here
        n = len(edges) + 1
        edge_distance = [[] for _ in range(n)]
        for edge in edges:
            p1, p2, d = edge
            edge_distance[p1].append((p2, d))
            edge_distance[p2].append((p1, d))

        distance = self.bfs(0, edge_distance, n)
        diameter_1 = self.find_max_index(distance)
        distance_diameter_1 = self.bfs(diameter_1, edge_distance, n)
        diameter_2 = self.find_max_index(distance_diameter_1)
        distance_diameter_2 = self.bfs(diameter_2, edge_distance, n)

        # print(distance_diameter_1)
        # print(distance_diameter_2)

        max_distance = 0
        for i in range(n):
            if i == diameter_1 or i == diameter_2:
                continue
            max_distance = max(max_distance, max(distance_diameter_1[i], distance_diameter_2[i]))

        return max_distance

    def find_max_index(self, distance):
        max_distance = 0
        index = 0

        for i in range(len(distance)):
            if distance[i] > max_distance:
                max_distance = distance[i]
                index = i

        return index

    def bfs(self, start_index, edge_distance, n):
        distance = [0] * n

        deque = collections.deque([start_index])
        visited = [False] * n
        visited[start_index] = True

        while deque:
            index = deque.popleft()
            cur_list = edge_distance[index]
            for i in range(len(cur_list)):
                p2, d = cur_list[i]
                if visited[p2] or d == -1:
                    continue
                deque.append(p2)
                visited[p2] = True
                distance[p2] = distance[index] + d

        return distance