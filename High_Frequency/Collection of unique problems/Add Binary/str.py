from collections import deque


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #         if not a:
        #             return b

        #         if not b:
        #             return a

        if a == "0" and b == "0":
            return "0"

        carry = 0
        a = int(a)
        b = int(b)
        result = deque()
        while a > 0 or b > 0:
            part_a = a % 10
            part_b = b % 10
            res = part_a + part_b + carry
            if res >= 2:
                carry = 1
                result.appendleft(str(res % 2))
            else:
                carry = 0
                result.appendleft(str(res))

            a = a // 10
            b = b // 10

        if carry == 1:
            result.appendleft(str(1))

        return "".join(result)

