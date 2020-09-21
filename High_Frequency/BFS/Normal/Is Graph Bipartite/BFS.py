from collections import deque


class Solution:
    # Edge case
    # 1. [] in set, meaning isolated, still valid
    # 2. two or more disconnected graphs
    # 3. []

    # 思路：
    # 1. 所有group初始化为0
    # 2. 扫描所有group，每当遇到0 -> 新的connected graph,当前点初始化，BFS
    # 2.1. 如果搜索到的下一个点group为0，设为当前点的对立group
    # 2.1. 如果next_node和node同group,false
    # 2.1. 不同group不变

    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True

        sets = [0] * len(graph)

        for i in range(len(graph)):
            if sets[i] == 0:
                queue = deque([i])
                sets[i] = -1
                while queue:
                    node = queue.popleft()
                    group = sets[node]
                    for next_node in graph[node]:
                        next_group = sets[next_node]
                        if next_group == 0:
                            sets[next_node] = -group
                            queue.append(next_node)
                        elif next_group == group:
                            return False

        return True