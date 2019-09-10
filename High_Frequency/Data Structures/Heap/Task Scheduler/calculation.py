from collections import Counter


class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """

    # O(time*logn) for heap, could be O(time) if input
    # to priority queue is sorted and a special algorithm
    # is used
    def leastInterval(self, tasks, n):
        # write your code here
        if not tasks:
            return 0

        if n == 0:
            return len(tasks)

        d = Counter(tasks)
        counts = list(d.values())
        longest = max(counts)
        longest_count = counts.count(longest)
        # maximum idle time
        # assume count(a) = b is the most
        # then the whole slot is like
        # axxx...
        # axxx...
        # ...
        # axx.. (This line only contains those count(x) = b)
        # In total we have b rows, where the last row might be significantly
        # shorter. All other elements are safe to be placed in the line before
        # the last line. Then we only need to calculate the idle time.
        # Note count(a) should also be deducted
        idle_time = (longest - 1) * (n + 1) + longest_count
        for time in counts:
            idle_time -= time
        return max(idle_time, 0) + len(tasks)
