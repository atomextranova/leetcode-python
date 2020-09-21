class Solution:
    """
    @param A: a integer sorted array
    @param B: a integer sorted array
    @param K: a integer
    @return: return a pair of index
    """

    def optimalUtilization(self, A, B, K):
        # write your code here
        if not A or not B:
            return []

        left = 0
        right = len(B) - 1
        cur_sum = A[0] + B[0]
        if cur_sum > K:
            return []

        if cur_sum == K:
            return [0, 0]

        left_index = 0
        right_index = 0

        while left < len(A) and right >= 0:
            while right >= 0 and (
                    (A[left] + B[right] > K) or (B[right] == B[right - 1])):
                right -= 1

            if right >= 0:
                if A[left] + B[right] <= K:
                    if A[left] + B[right] > cur_sum:
                        cur_sum = A[left] + B[right]
                        left_index = left
                        right_index = right
            left += 1

        return [left_index, right_index]


