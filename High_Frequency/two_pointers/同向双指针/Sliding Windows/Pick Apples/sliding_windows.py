class Solution:
    """
    @param A: a list of integer
    @param K: a integer
    @param L: a integer
    @return: return the maximum number of apples that they can collect.
    """

    def PickApples(self, A, K, L):
        # write your code here
        length = len(A)
        if K + L > length:
            return -1

        cur_sum = 0
        prefix_sums = [0] * length
        suffix_sums = [0] * length
        for i in range(length):
            cur_sum += A[i]
            prefix_sums[i] = cur_sum

        cur_sum = 0
        for i in range(length - 1, -1, -1):
            cur_sum += A[i]
            suffix_sums[i] = cur_sum

        suffix_sums = suffix_sums[::-1]

        max_1 = self.pick_apple_util(A, K, L, prefix_sums, suffix_sums)
        max_2 = self.pick_apple_util(A, L, K, prefix_sums, suffix_sums)

        return max(max_1, max_2)

    def pick_apple_util(self, A, K, L, prefix, suffix):
        length = len(A)
        max_array_length = length - K - L + 1
        prefix_max = [0] * max_array_length
        suffix_max = [0] * max_array_length
        prefix_max[0] = prefix[K - 1]
        suffix_max[0] = suffix[L - 1]

        for i in range(1, max_array_length):
            prefix_max[i] = max(prefix_max[i - 1],
                                prefix[i + K - 1] - prefix[i - 1])
            suffix_max[i] = max(suffix_max[i - 1],
                                suffix[i + L - 1] - suffix[i - 1])

        sums = [prefix_max[i] + suffix_max[max_array_length - i - 1] for i in
                range(max_array_length)]
        return max(sums)