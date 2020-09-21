import math

class Solution:
    def primePalindrome(self, N: int) -> int:
        i = N
        while True:
            n = str(i)
            length = len(n)
            # Skip even length number since always
            # divisble by 11

            # Remember spicial case 11
            if length % 2 == 0 and i > 11:
                i = int(math.pow(10, length))
                continue
            if self.check(n) and self.is_prime(i):
                return n
            i += 1

    def is_prime(self, i):
        if i == 1:
            return False
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                return False

        return True

    def check(self, n):
        return n == n[::-1]