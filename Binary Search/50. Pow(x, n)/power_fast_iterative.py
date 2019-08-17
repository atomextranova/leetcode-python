class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """

    def myPow(self, x, n):
        result = 1
        if n < 0:
            temp_val = 1/x
            n = -n
        else:
            temp_val = x

        while n != 0:
            bit = n & 1

            if bit != 0:
                result *= temp_val
            temp_val *= temp_val
            n = n // 2
        return result

sol = Solution()
print(sol.myPow(8.854, -5))
