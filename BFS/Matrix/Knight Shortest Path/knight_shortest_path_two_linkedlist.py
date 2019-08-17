"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and Triangle Count (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """
    # Key point
    # Triangle Count. linked list to implement BFS: generate all possible move of current step
    # (route length n) and push to next linked list (length n + Triangle Count)
    # 2. Check all possible next step is valid
    # 3. check destination
    # 4. No edge case check: What if cannot return with reasonable step? Or too many possible cases?
    def shortestPath(self, grid, source, destination):
        # write your code here
        self.row_length = len(grid)
        self.column_length = len(grid[0])
        grid_temp = grid # Could use a copy here
        source_x, source_y = source.x, source.y
        destination_x, destination_y = destination.x, destination.y
        source_temp = (source_x, source_y)
        destination_temp = (destination_x, destination_y)
        if self.is_destination(source_temp, destination_temp):
            return 0
        next_step_queue = [source_temp]
        temp_queue = []
        length = 0
        while next_step_queue:
            length += 1
            while next_step_queue:
                x, y = next_step_queue.pop(0)
                for x_shift in [-2, -1, 1, 2]:
                    for direction in [-1, 1]:
                        y_shift = (3 - abs(x_shift)) * direction
                        x_next = x + x_shift
                        y_next = y + y_shift
                        next_try = (x_next, y_next)
                        if self.is_valid(next_try):
                            # Slow because cannot check if visited first
                            if grid_temp[x_next][y_next] == 0:
                                if self.is_destination(next_try, destination_temp):
                                    return length
                                else:
                                    temp_queue.append(next_try)
                                    grid_temp[x_next][y_next] = 1
            next_step_queue, temp_queue = temp_queue, next_step_queue
        return -1

    def is_destination(self, current, destination):
        return current[0] == destination[0] and current[1] == destination[1]

    def is_valid(self, next_try):
        return self.row_length > next_try[0] >= 0 and self.column_length > next_try[1] >= 0
