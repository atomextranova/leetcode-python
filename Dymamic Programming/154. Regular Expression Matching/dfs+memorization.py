class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """

    def isMatch(self, s, p):
        # write your code here
        s_length = len(s)
        p_length = len(p)

        if not s:
            for char in p:
                if char != "*":
                    return False
            return True

        if not p:
            return s_length == 0

        memo = {}

        return self.dfs(s, p, s_length, p_length, 0, 0, memo)

    def dfs(self, s, p, s_length, p_length, s_index, p_index, memo):

        if (s_index, p_index) in memo:
            return memo[(s_index, p_index)]

        # pattern used up
        if p_index == p_length:
            return s_length == s_index

        # string used up, the rest of pattern must all be x*y*..
        if s_index == s_length:
            # key: deal with odd number first
            if (p_length - p_index) % 2 == 1:
                return False
            # if even, can safely check if all odd index is #
            i = p_index + 1
            while i < p_length:
                if p[i] != "*":
                    return False
                i += 2
            return True

        memo[(s_index, p_index)] = False

        sub_pattern = p[p_index]
        sub_str = s[s_index]

        if p_index + 1 < p_length and p[p_index + 1] == "*":
            # continue use * or not (key)
            # 1. continue using # for current char in str
            # 2. not use # for current char in str
            memo[(s_index, p_index)] = self.char_match(sub_str,
                                                       sub_pattern) and self.dfs(
                s, p, s_length, p_length,
                s_index + 1, p_index, memo,
                ) or \
                                       self.dfs(s, p, s_length, p_length,
                                                s_index, p_index + 2,
                                                memo)

        else:
            memo[(s_index, p_index)] = self.dfs(s, p, s_length, p_length,
                                                s_index + 1, p_index + 1, memo,
                                                ) and self.char_match(
                sub_str, sub_pattern)

        return memo[(s_index, p_index)]

    def char_match(self, sub_str, sub_pattern):
        return sub_str == sub_pattern or sub_pattern == "."