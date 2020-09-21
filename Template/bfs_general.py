# python模版## Python普通BFS模版
# 创建所需数据结构
queue = collections.deque()
visited = set()

# 初始化，将初始点加入队列和visited
queue.append(0)
visited.add(0)

while queue:
    now = queue.popleft()
    # 找所有当前点能一步到达的点
    for next_point in self.find_next(now):
        # 不满足条件直接跳过
        if not self.is_valid(now):
            continue
        # 若满足条件，加入队列同时更新visited
        queue.append(next_point)
        visited.add(next_point)





## Python进阶BFS模版
# 创建所需数据结构
queue = collections.deque()
visited = set()

# 初始化，将初始点加入队列和visited
queue.append(0)
visited.add(0)

while queue:
    for i in range(len(queue)):
        now = queue.popleft()
        # 找所有当前点能一步到达的点
        for next_point in self.find_next(now):
            # 不满足条件直接跳过
            if not self.is_valid(now):
                continue
            # 若满足条件，加入队列同时更新visited
            queue.append(next_point)
            visited.add(next_point)

## Python BFS字典模版
# 创建所需数据结构
queue = collections.deque()
distance = {}

# 初始化，将初始点加入队列和visited
queue.append(0)
distance[0] = 0

while queue:
    now = queue.popleft()
    # 找所有当前点能一步到达的点
    for next_point in self.find_next(now):
        # 不满足条件直接跳过
        if not self.is_valid(now):
            continue
        # 若满足条件，加入队列同时更新visited
        queue.append(next_point)