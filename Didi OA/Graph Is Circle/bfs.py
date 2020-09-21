class Solution:

    def isCircle(self, start_list, end_list):
        if not start_list or not end_list:
            return False

        start_to_end = {}
        for i in range(len(start_list)):
            start = start_list[i]
            end = end_list[i]
            if start in start_to_end:
                return False
            start_to_end[start] = end

        start_point = start
        start = start_to_end[start]
        distance = 1
        while start_point != start:
            start = start_to_end[start]
            distance += 1

        return distance == len(start_list)

sol = Solution()

assert sol.isCircle([1], [1])
assert sol.isCircle([3, 1, 2], [2, 3, 1])
assert not sol.isCircle([1, 2, 1], [2, 3, 3])
assert not sol.isCircle([1, 2, 3, 4], [2, 1, 4, 4])
assert not sol.isCircle([1, 2, 3, 4], [2, 1, 4, 3])
assert not sol.isCircle([1, 2, 2, 3, 3], [2, 3, 3, 4, 5])