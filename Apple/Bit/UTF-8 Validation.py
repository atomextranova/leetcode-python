from typing import List

class Solution:
    def rshift(self, val, n):
        return (val % 0x100000000) >> n

    # While loop
    # First count number of 1s in first line
    # If > 5 or = 1: return False (When only 1 byte, no 1s)
    # If = 0: byte_count = 1
    # Then check if enough number of data exists in array
    # If enough
    # for each next, check (num & 2 << 6) ? 2<< 6
    # (Checks for 10XXXXXX)
    def validUtf8(self, data: List[int]) -> bool:
        if not data:
            return True

        i = 0
        length = len(data)
        while i < len(data):
            num = data[i]
            byte_count = 0
            # print(num & 128)
            # print(bin(num))
            # print(bin(num & 128))
            while num & 128 == 128:
                num = num << 1
                num = num & 255
                # print(bin(num))
                byte_count += 1
            if byte_count == 1 or byte_count > 4:
                return False
            if byte_count == 0:
                byte_count = 1

            # print(bin(num))
            print(byte_count)
            # print(byte_count)
            if i + byte_count > length:
                # print("Not enough")
                return False

            for j in range(i + 1, i + byte_count):
                # print(bin(data[j]))
                # print(self.rshift(data[i+j+1], 6))

                if (data[j] & (2 << 6)) != (2 << 6):
                    return False

            i += byte_count

        return True
    
sol = Solution()
print(sol.validUtf8([197, 130, 1]))