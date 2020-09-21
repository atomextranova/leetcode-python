class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """

    def isHappy(self, n):
        # write your code here
        if n == 1:
            return True
        slow = self.happy(n)
        fast = self.happy(self.happy(n))
        while slow != fast and slow != 1 and fast != 1:
            slow = self.happy(slow)
            fast = self.happy(self.happy(fast))

        return fast == 1

    def happy(self, n):
        result = 0
        while n > 0:
            result += (n % 10) ** 2
            n = n // 10
        return result