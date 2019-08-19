"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def minMeetingRooms(self, intervals):
        # Write your code here
        if not intervals:
            return 0

        time = []
        for interval in intervals:
            time.append((interval.start, 1))
            time.append((interval.end, -1))

        time.sort(key=lambda x: (x[0], x[1]))

        cur_room = 0
        max_room = 0
        for _, value in time:
            cur_room += value
            max_room = max(max_room, cur_room)

        return max_room