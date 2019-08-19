"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def countOfAirplanes(self, airplanes):
        # write your code here

        if not airplanes:
            return 0

        time = []
        for airplane in airplanes:
            time.append((airplane.start, 1))
            time.append((airplane.end, -1))

        time.sort(key=lambda x: (x[0], x[1]))

        cur_plane = 0
        max_plane = 0
        for _, value in time:
            cur_plane += value
            max_plane = max(max_plane, cur_plane)

        return max_plane