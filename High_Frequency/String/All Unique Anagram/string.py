class Solution:
    """
    @param s: a string
    @param p: a string
    @return: a list of index
    """

    def findAnagrams(self, s, p):
        # write your code here
        # if s empty, p is defined non-empty
        if not s:
            return []

        # len(p) > len(s)
        if len(p) > len(s):
            return []

        # construct p's stats about chars
        char_dict = [0] * 26
        for char in p:
            char_dict[self.index(char)] += 1

        # initialize the window and check (first possible match string, start
        # from 0)
        length_p = len(p)
        for i in range(length_p):
            char_dict[self.index(s[i])] -= 1
        result = []
        start = 0
        if self.match(char_dict):
            result.append(start)

        # Slide window to check the rest
        # Could be optimized (match())
        for i in range(length_p, len(s)):
            start += 1
            char_dict[self.index(s[i])] -= 1
            char_dict[self.index(s[i - length_p])] += 1
            if self.match(char_dict):
                result.append(start)
        return result

    def index(self, char):
        return ord(char) - ord("a")

    def match(self, char_dict):
        return sum([abs(n) for n in char_dict]) == 0