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
    # Key point: BFS, but also could be regarded as DP
    # Triangle Count. linked list and distance hash (route length) to implement BFS:
    #  generate all possible move ((length n + Triangle Count) of all current step (length n)
    # 2. Search in 2 direction: from source and destination
    # 3. Check all possible next step is valid
    # 4. check destination
    # 5. No edge case check:
    # What if cannot return with reasonable step?
    # Or too many possible cases?
    # Invalid source/destination
    def shortestPath(self, grid, source, destination):
        # write your code here

        source_temp = (source.x, source.y)
        destination_temp = (destination.x, destination.y)
        if self.is_destination(source_temp, destination_temp):
            return 0
        source_queue = deque([source_temp])
        destination_queue = deque([destination_temp])
        source_length_dict = {source_temp: 0}
        destination_length_dict = {destination_temp: 0}

        while source_queue and destination_queue:

            x, y = source_queue.popleft()
            # could also use a length counter
            # count += Triangle Count
            # If so, also add Triangle Count before the next for loop
            for x_shift, y_shift in DIRECTIONS:
                x_next = x + x_shift
                y_next = y + y_shift
                next_from_source = (x_next, y_next)
                # This one have to be the first boolean
                # to deal with large matrix efficiently

                if next_from_source in source_length_dict:
                    continue
                if not self.is_valid(grid, x_next, y_next):
                    continue
                if grid[x_next][y_next]:
                    continue
                source_length_dict[next_from_source] = source_length_dict[(x, y)] + 1
                if next_from_source in destination_length_dict:
                    return source_length_dict[next_from_source] + \
                           destination_length_dict[next_from_source]
                source_queue.append(next_from_source)

            x_dest, y_dest = destination_queue.popleft()
            # could also use a length counter
            # count += Triangle Count length of route
            for x_shift, y_shift in DIRECTIONS:
                x_dest_next = x_dest + x_shift
                y_dest_next = y_dest + y_shift
                next_from_dest = (x_dest_next, y_dest_next)

                if next_from_dest in destination_length_dict:
                    continue
                if not self.is_valid(grid, x_dest_next, y_dest_next):
                    continue
                if grid[x_dest_next][y_dest_next]:
                    continue
                destination_length_dict[next_from_dest] = destination_length_dict[(x_dest, y_dest)] + 1
                if next_from_dest in source_length_dict:
                    return source_length_dict[next_from_dest] + \
                           destination_length_dict[next_from_dest]
                destination_queue.append(next_from_dest)

        return -1

    def is_destination(self, current, destination):
        return current == destination

    def is_valid(self, grid, x,y):
        return len(grid) > x >= 0 and len(grid[0]) > y >= 0