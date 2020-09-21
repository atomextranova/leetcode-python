class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """
    def copyBooksII(self, n, times):
        # write your code here
        max_time = max(times)
        start = 0
        end = n * max_time

        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_valid(n, times, mid):
                end = mid
            else:
                start = mid

        if self.is_valid(n, times, start):
            return start
        else:
            return end

    def is_valid(self, n, times, plan):
        count = 0
        for time in times:
            count += plan // time

        return count >= n