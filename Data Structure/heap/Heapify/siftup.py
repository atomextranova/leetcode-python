import sys
import collections

# O(nlogn)
class Solution:
    # @param A: Given an integer array
    # @return: void
    def siftup(self, A, k):
        while k != 0:
            father = (k - 1) // 2
            if A[k] > A[father]:
                break
            temp = A[k]
            A[k] = A[father]
            A[father] = temp

            k = father

    def heapify(self, A):
        for i in range(len(A)):
            self.siftup(A, i)