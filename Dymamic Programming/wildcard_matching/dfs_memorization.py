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

        # string used up, the rest of pattern must all be *
        if s_index == s_length:
            for i in range(p_index, p_length):
                if p[i] != "*":
                    return False
            return True

        # pattern used up
        if p_index == p_length:
            return s_length == s_index

        memo[(s_index, p_index)] = False

        sub_pattern = p[p_index]
        sub_str = s[s_index]

        if sub_pattern == "*":
            # continue use * or not (key)
            # 1. continue using # for current char in str
            memo[(s_index, p_index)] = self.dfs(s, p, s_length, p_length,
                                                s_index + 1, p_index, memo,
                                                ) or \
                                       self.dfs(s, p, s_length, p_length,
                                                s_index, p_index + 1,
                                                memo, )
            # 2. not use # for current char in str
        else:
            memo[(s_index, p_index)] = self.dfs(s, p, s_length, p_length,
                                                s_index + 1, p_index + 1, memo,
                                                ) and self.char_match(
                sub_str, sub_pattern)

        return memo[(s_index, p_index)]

    def char_match(self, sub_str, sub_pattern):
        return sub_str == sub_pattern or sub_pattern == "?"
