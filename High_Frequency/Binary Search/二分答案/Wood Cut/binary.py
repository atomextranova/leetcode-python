class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if not L:
            return 0

        max_val = max(L)
        min_val = 0

        while min_val + 1 < max_val:
            mid_val = (max_val + min_val) // 2
            if self.valid(L, k, mid_val):
                min_val = mid_val
            else:
                max_val = mid_val

        if self.valid(L, k, max_val):
            return max_val
        else:
            return min_val

    def valid(self, L, k, mid_val):
        count = 0
        for l in L:
            count += l // mid_val

        return count >= k