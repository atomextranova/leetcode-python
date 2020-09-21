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
        indexA, indexB = 0, 0
        for i in range(len(A)):
            summ = A[indexA] + B[indexB]
            for j in range(len(B)):
                if K == A[i] + B[j]:
                    return [i, j]
                elif K > A[i] + B[j]:
                    if A[i] + B[j] > summ:
                        indexA, indexB = i, j
                        summ = A[indexA] + B[indexB]
                else:
                    break
        return [indexA, indexB]