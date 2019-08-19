class Solution:
    """
    @param x: a double
    @return: the square root of x
    """

    def sqrt(self, x):
        # write your code here
        if x > 1:
            low, high = 1, x
        else:
            low, high = x, 1

        mid = (low + high) / 2

        while (high - low) > 1e-10:
            if mid ** 2 > x:
                high = mid
            else:
                low = mid
            mid = (low + high) / 2

        return mid