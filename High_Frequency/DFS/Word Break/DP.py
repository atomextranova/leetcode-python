class Solution:
    """
    @param s: A string
    @param wordSet: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, wordSet):
        # write your code here

        if not s:
            return True

        if not wordSet:
            return False

        memo = dict()
        min_length = float('inf')
        max_length = float('-inf')
        s_length = len(s)
        for word in wordSet:
            length = len(word)
            min_length = min(min_length, length)
            max_length = max(max_length, length)
        dp_table = [False] * (s_length + 1)
        dp_table[0] = True

        for i in range(1, s_length + 1):
            index = i - 1
            if not dp_table[index]:
                continue
            for j in range(index + min_length, index + max_length + 1):
                if j > s_length:
                    break
                part = s[index:j]
                if part in wordSet:
                    dp_table[j] = dp_table[index]

        return dp_table[-1]