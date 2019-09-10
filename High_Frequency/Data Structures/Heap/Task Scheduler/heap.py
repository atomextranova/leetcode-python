from collections import defaultdict
from heapq import heappush, heappop


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

        char_to_count = defaultdict(int)
        for task in tasks:
            char_to_count[task] += 1

        task_heap = []
        for task, value in char_to_count.items():
            if value != 0:
                heappush(task_heap, (-value, task))

        time = 0

        # insert/remove = O(logn)
        # could also sort every time
        while len(task_heap) != 0:
            cur_time = 0
            unfinished_list = []
            # <=
            while cur_time <= n and len(task_heap) != 0:
                value, task = heappop(task_heap)
                cur_time += 1
                value += 1
                if value != 0:
                    unfinished_list.append((value, task))

            # Must continue here because there might be
            # some single character
            # left in the heap. In such case, no idle time
            # needed.
            if len(unfinished_list) == 0:
                time += cur_time
                continue
            # Some unfinished = need idle time
            time += n + 1
            for value_task in unfinished_list:
                heappush(task_heap, value_task)

        return time