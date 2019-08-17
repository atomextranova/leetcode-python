# 信封存在两个维度，首先贪心按照其中一个维度将信封排序，
# 一个维然后在另度上面寻找最长上升子序列。
# 此处使用二分优化最长上升子序列，
# 在dp数组中二分查找h的位置，dp[i] = h，
# 当i = length，说明插入位置为最后，则length += 1。

def bisect_left(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo

class Solution:
    # @param {int[][]} envelopes a number of envelopes with widths and heights
    # @return {int} the maximum number of envelopes
    def maxEnvelopes(self, envelopes):
        # Write your code here
        height = [a[1] for a in sorted(envelopes, key = lambda x: (x[0], -x[1]))]
        dp, length = [0] * len(height), 0

        import bisect
        for h in height:
            i = bisect.bisect_left(dp, h, 0, length)
            dp[i] = h
            if i == length:
                length += 1
        return length