class Solution:
    """
    @param s: the string that represents a number
    @return: whether the string is a valid number
    """

    # Edge case:
    # Leading +/- True
    # 1. / .1 True
    # 2e10/2e-10/2E10/2E-10 True
    # Not 0-9, e, E, +, -, . False
    # . False
    # .xxx.xx False
    # 1 1 False
    # E E False
    def isNumber(self, s):
        # write your code here
        index = 0
        s = s.strip()
        length = len(s)

        if length == 0:
            return False
        if s in [".", "E", "e"]:
            return False

        print("done")

        if s[index] in ["+", "-"]:
            index += 1

        num_digits = 0
        num_point = 0
        while index < length:
            if s[index].isdigit():
                num_digits += 1
            elif s[index] == ".":
                num_point += 1
            else:
                break
            index += 1

        if num_digits == 0 or num_point > 1:
            return False

        if index == length:
            return True

        if not s[index].isdigit() or not s[index] in [".", "E", "e"]:
            return False

        num_digits = 0
        num_point = 0
        while index < length:
            if s[index] in ["E", "e"]:
                index += 1
                if s[index] in ["+", "-"]:
                    index += 1
            if s[index].isdigit():
                num_digits += 1
            elif s[index] == ".":
                num_point += 1
            else:
                return False

        if num_digits == 0 or num_point > 1:
            return False

        return index == length

