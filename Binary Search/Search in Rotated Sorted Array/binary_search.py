class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """

    def search(self, A, target):
        # write your code here
        if not A:
            return -1

        start = 0
        end = len(A) - 1

        start_val = A[start]
        end_val = A[end]

        while start + 1 < end:
            mid = start + ((end - start) >> 1)
            mid_val = A[mid]
            print(mid)
            if mid_val == target:
                return mid
            # first decide mid_val > start_val => start_val -> mid_val -> max -> end_val
            # else start_val -> max -> mid_val -> end_val
            if mid_val > start_val:
                # = is inclusive
                if start_val <= target <= mid_val:
                    end = mid
                    end_val = mid_val
                else:
                    start = mid
                    start_val = mid_val

            else:
                if end_val >= target >= mid_val:
                    start = mid
                    start_val = mid_val
                else:
                    end = mid
                    end_val = mid_val

        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1



sol = Solution()
print(sol.search([6,8,9,1,3,5], 5))