class Solution:

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        answer = 1
        temp_value = x
        while n > 0:
            power_two = n % 2
            if power_two == 1:
                answer *= temp_value
            temp_value *= temp_value
            n = n // 2
        return answer