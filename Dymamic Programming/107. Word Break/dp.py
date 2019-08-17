# 滚动数组

class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, dict):
        # write your code here
        max_length = 0
        for word in dict:
            max_length = max(max_length, len(word))
        length = len(s)
        is_possible = [False] * (length + 1)
        is_possible[0] = True

        for i in range(1, length + 1):
            for j in range(1, min(i, max_length) + 1):
                if not is_possible[i - j]:
                    continue
                if s[i - j:i] in dict:
                    is_possible[i] = True
                    break

        return is_possible[length]