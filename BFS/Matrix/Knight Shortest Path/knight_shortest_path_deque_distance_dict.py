"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

DIRECTIONS = [
    (-2, -1), (-2, 1), (-1, 2), (1, 2),
    (2, 1), (2, -1), (1, -2), (-1, -2),
]

from collections import deque

class Solution:
    """
    @param grid: a chessboard included 0 (false) and Triangle Count (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """
    # Key point
    # Triangle Count. linked list and distance hash (route length) to implement BFS:
    #  generate all possible move ((length n + Triangle Count) of all current step (length n)
    # 2. Check all possible next step is valid
    # 3. check destination
    # 4. No edge case check:
    # What if cannot return with reasonable step?
    # Or too many possible cases?
    # Invalid source/destination
    def shortestPath(self, grid, source, destination):
        # write your code here
        source_temp = (source.x, source.y)
        destination_temp = (destination.x, destination.y)
        next_step_queue = deque([source_temp])
        length_dict = {(source.x, source.y): 0}
        if self.is_destination(source_temp, destination_temp):
            return 0
        while next_step_queue:
            x, y = next_step_queue.popleft()
            if self.is_destination((x, y), destination_temp):
                return length_dict[(x, y)]
            for x_shift, y_shift in DIRECTIONS:
                x_next = x + x_shift
                y_next = y + y_shift
                # This one have to be the first check
                # to deal with large matrix efficiently (many repeated search)
                if (x_next, y_next) not in length_dict:
                    if self.is_valid(grid, x_next, y_next):
                        if not grid[x_next][y_next]:
                            length_dict[(x_next, y_next)]= length_dict[(x, y)] + 1
                            next_step_queue.append((x_next, y_next))
        return -1

    def is_destination(self, current, destination):
        return current == destination

    def is_valid(self, grid, x,y):
        return len(grid) > x >= 0 and len(grid[0]) > y >= 0