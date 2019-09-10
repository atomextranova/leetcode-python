# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        start = 0
        end = n
        while start + 1 < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid

        if isBadVersion(start):
            return start
        else:
            return end
