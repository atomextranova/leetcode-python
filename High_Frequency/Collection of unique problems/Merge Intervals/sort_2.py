class Solution:

    # Sort the intervals first
    # Then merge intervals if needed
    # Add to result after a new interval that cannot be merged
    # Appears
    # Add the last [start, end] to result
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        intervals.sort(key=lambda x: x[0])
        print(intervals)
        result = []
        start = 0
        end = 0
        first = True
        for interval in intervals:
            if first:
                start, end = interval
                first = False
            else:
                if interval[0] <= end:
                    end = max(end, interval[1])
                else:
                    result.append([start, end])
                    start, end = interval
        # Append the last element
        result.append([start, end])

        return result