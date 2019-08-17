class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndexII(self, A):
        # write your code here
        result = 1
        permutation = 1
        repeat_factor = 1
        used_table = {}
        for i in range(len(A) - 1, -1, -1):
            current_val = A[i]
            used_table.setdefault(current_val, 0)
            # Combination = n! / (a! * b!...*x!)
            used_table[current_val] += 1
            repeat_factor *= used_table[current_val]
            smaller = 0
            for j in range(i + 1, len(A)):
                if A[j] < current_val:
                    smaller += 1
            result += smaller * permutation // repeat_factor
            permutation *= len(A) - i
        return result
