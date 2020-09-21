class Solution:
    """
    @param a: an array
    @param k: the kth
    @return: return the kth subarray
    """

    def thekthSubarray(self, a, k):
        # wrrite your code here
        cur_sum = 0
        length = len(a)
        prefix = [0] * (length + 1)
        for i in range(1, length + 1):
            cur_sum += a[i - 1]
            prefix[i] = cur_sum
        self.prefix = prefix
        self.a = a
        min_val = 0
        max_val = prefix[-1]
        total = (length + 1) * length // 2

        while min_val + 1 < max_val:
            mid_val = (min_val + max_val) // 2
            if self.check_at_least_k(mid_val, k, prefix, length, total):
                max_val = mid_val
            else:
                min_val = mid_val
            # print(min_val, max_val)
        print(min_val, max_val)
        return max_val

    def check_at_least_k(self, val, k, prefix, length, total):
        right = 1
        count = 0
        print("mid:", val)
        for left in range(length):
            while right < (length + 1) and prefix[right] - prefix[left] <= val:
                right += 1

            if right < (length + 1):
                print(self.a[left:right])
                count += length - right + 1

        print(total - count)

        if total - count >= k:
            return True

        return False

sol = Solution()
sol.thekthSubarray([2,3,1,4], 6)
