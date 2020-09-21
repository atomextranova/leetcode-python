class Solution:

    # Key observation
    # 0 and 1 are useless
    # 2*2*2 < 3*3, 2*2 >> 3*1 => no more than two 2s(thre 2s can be two 3s)
    # for any f >= 4, f <= 2f-4 = 2*(f-2)

    # O(logn) for power function
    def integerBreak(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        if n == 3:
            return 2

        factor = int(n / 3)
        remainder = n % 3

        if remainder == 1:
            remainder = 4
            factor -= 1
        elif remainder == 0:
            remainder = 1

        return int(math.pow(3, factor) * remainder)