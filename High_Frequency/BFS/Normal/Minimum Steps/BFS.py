from collections import deque


class Solution:
    """
    @param colors: the colors of grids
    @return: return the minimum step from position 0 to position n - 1
    """
    # Standard BFS
    # 1. Create a dict for indexes with the same num
    # 2. Start standard BFS by layer, note
    # a. to include indexes if the current num is present in the dict
    # b. to exclude indexes of current num when jump
    # return once found the step

    # Time: O(n)
    # Space: O(n)
    def minimumStep(self, colors):
        # write your code here
        if not colors:
            return 0

        visited = set()
        length = len(colors)
        target = length - 1
        step = 0
        color_to_indexes = {}
        to_be_tried = deque([0])

        for i, color in enumerate(colors):
            if color not in color_to_indexes:
                color_to_indexes[color] = []
            color_to_indexes[color].append(i)

        while to_be_tried:

            for i in range(len(to_be_tried)):
                index = to_be_tried.popleft()
                if index in visited:
                    continue

                if index == target:
                    return step

                visited.add(index)
                if self.check_valid(index - 1, visited, length):
                    to_be_tried.append(index - 1)
                if self.check_valid(index + 1, visited, length):
                    to_be_tried.append(index + 1)
                cur_color = colors[index]
                if cur_color in color_to_indexes:
                    to_be_tried.extend(color_to_indexes[cur_color])
                    del color_to_indexes[cur_color]

            step += 1

        return -1

    def check_valid(self, index, visited, length):
        return -1 < index < length and index not in visited
