
# data represents something to search on

from collections import deque

def bfs(start):
    queue = deque([start])
    visited = set()
    visited.add(start)
    while queue:
        length = len(queue)
        # Level order search
        for _ in range(length):
            element = queue.popleft()
            for next in next_step(element):
                if not check(next, visited):
                    continue
                # if valid and not visited, keep searching
                queue.append(element)
                visited.add(next)

# check whether next step is valid or in visited
def check(element, visited):
    return

# return next step element
def next_step(element):
    return