from heapq import heappush, heappop


class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """

    # Time: O(n)
    # Space: O(1)
    def trapRainWater(self, heights):
        # write your code here
        min_heap = []
        result = 0
        row_number = len(heights)
        column_number = len(heights[0])
        print(row_number)
        print(column_number)
        visited = set()

        # index - 1
        for i in range(column_number):
            self.add_heap(min_heap, visited, heights[0][i], 0, i)
            self.add_heap(min_heap, visited, heights[row_number - 1][i],
                          row_number - 1, i)

        for i in range(row_number):
            self.add_heap(min_heap, visited, heights[i][0], i, 0)
            self.add_heap(min_heap, visited, heights[i][column_number - 1], i,
                          column_number - 1)

        delta_list = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while len(min_heap) > 0:
            lowest_height, x, y = heappop(min_heap)
            for dx, dy in delta_list:
                new_x, new_y = (x + dx, y + dy)
                if not self.inside(new_x, new_y, row_number, column_number):
                    continue
                if (new_x, new_y) in visited:
                    continue
                height = heights[new_x][new_y]
                self.add_heap(min_heap, visited, height, new_x, new_y)
                result += max(0, lowest_height - height)
                print("result: %d, x: %d, y: %d, height: %d" % (result, new_x, new_y, height))

        return result

    def add_heap(self, min_heap, visited, height, x, y):
        heappush(min_heap, (height, x, y))
        visited.add((x, y))

    def inside(self, new_x, new_y, row_number, column_number):
        return 0 < new_x < row_number and 0 < new_y < column_number
