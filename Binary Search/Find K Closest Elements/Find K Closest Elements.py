class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A, target, k):
        # write your code here
        if not A:
            return []

        start = 0
        end = len(A) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        result = []
        low = start
        high = end
        while k > 0:
            if high >= len(A):
                result.append(A[low])
                low -= 1
            elif low < 0:
                result.append(A[high])
                high += 1
            else:
                low_val = A[low]
                high_val = A[high]
                if target - low_val <= high_val - target:
                    result.append(low_val)
                    low -= 1
                else:
                    result.append(high_val)
                    high += 1
            k -= 1
        return result