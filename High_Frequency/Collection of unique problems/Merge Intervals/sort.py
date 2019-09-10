"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """

    def merge(self, intervals):
        # write your code here
        if not intervals:
            return []

        merged = []
        intervals.sort(key=lambda x: (x.start, x.end))

        for interval in intervals:
            # Append if not overlapping
            while not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                # Choose the larger end
                merged[-1].end = max(interval.end, merged[-1].end)

        return merged
