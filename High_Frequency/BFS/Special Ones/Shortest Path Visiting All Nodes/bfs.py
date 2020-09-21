import collections

class Solution:
    """
    @param graph: the graph
    @return: the shortest path for all nodes
    """
    def shortestPathLength(self, graph):
        # Write your code here.
        visited = [{} for _ in range(len(graph))]
        full_path = (1 << len(graph)) - 1
        min_distance = float('inf')
        for i in range(len(graph)):
            deque = collections.deque([(0, 0 | (1 << i), i, str(i))])
            visited[i][0 | (1 << i)] = 0

            while deque:
                distance, path, index, s = deque.popleft()
                if path == full_path:
                    min_distance = min(min_distance, distance)
                    break

                for next_index in graph[index]:
                    next_path = path | (1 << next_index)
                    next_distance = distance + 1

                    if next_path in visited[next_index] and visited[next_index][next_path] <= next_distance:
                        continue

                    visited[next_index][next_path] = next_distance
                    deque.append((next_distance, next_path, next_index, s+str(next_index)))

        return min_distance if min_distance != float('inf') else -1



