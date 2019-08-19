"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param seqA: the list of intervals
    @param seqB: the list of intervals
    @return: the time periods
    """

    def timeIntersection(self, seqA, seqB):
        # Write your code here
        if not seqA or not seqB:
            return []

        time = []
        # Initialize
        for interval in seqA:
            time.append((interval.start, 1))
            time.append((interval.end, -1))

        for interval in seqB:
            time.append((interval.start, 1))
            time.append((interval.end, -1))

        time.sort(key=lambda x: (x[0], x[1]))
        cur_online = 0
        intersection_intervals = []
        last_time = -1
        for time, value in time:
            # Make sure calculate interval before -1
            # which is the end time
            if cur_online == 2:
                self.merge(last_time, time, intersection_intervals)
            cur_online += value

            last_time = time

        return intersection_intervals

    def merge(self, last_time, time, intersection_intervals):
        # When no interval could be found (last_time = -1) or no need to merge
        if last_time < 0 or last_time == time:
            return

        # When no element, avoid index out of range
        if len(intersection_intervals) > 1 and intersection_intervals[
            -1].end == last_time:
            intersection_intervals[-1].end = time

        intersection_intervals.append(Interval(last_time, time))