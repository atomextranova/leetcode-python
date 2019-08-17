class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        # write your code here
        start_index = 0
        end_index = len(A) - 1

        while start_index + 1 < end_index:
            mid_index = start_index + (end_index - start_index) // 2
            mid_val = A[mid_index]
            left_index = mid_index - 1
            right_index = mid_index + 1
            left_val = A[left_index]
            right_val = A[right_index]

            if left_val < mid_val:
                start_index = mid_index
            elif right_val < mid_val:
                end_index = mid_index
            else:
                end_index = mid_index

        if A[start_index] < A[end_index]:
            return end_index
        else:
            return start_index

sol = Solution()
print(sol.findPeak([1,2,1,2,3,1]))