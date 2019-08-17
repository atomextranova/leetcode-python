class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        # write your code here
        result = 1
        permutation = 1
        for i in range(len(A) - 1, -1, -1):
            current_val = A[i]
            smaller = 0
            for j in range(i + 1, len(A)):
                if A[j] < current_val:
                    smaller += 1
            # First element is smaller than next val, others will be permutation
            result += smaller * permutation
            permutation *= len(A) - i
        return result