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

        is_possible = [[False] * (p_length + 1) for _ in range(s_length + 1)]
        is_possible[0][0] = True

        any_match_list = ["*", "?"]

        for i in range(0, s_length + 1):
            for j in range(0, p_length + 1):
                if j > 0:
                    # 多个连续* match 一个字符
                    is_possible[i][j] = is_possible[i][j] or \
                                        (is_possible[i][j - 1] and p[j - 1] == "*")

                if i > 0 and j > 0:
                    # 一个* match 多个字符
                    is_possible[i][j] = is_possible[i][j] or \
                                        (is_possible[i - 1][j] and p[j - 1] == "*")

                    # 单个字符match
                    is_possible[i][j] = is_possible[i][j] or \
                                        (is_possible[i - 1][j - 1] and (
                                                    p[j - 1] == s[i - 1] or p[j - 1] in any_match_list))

        return is_possible[s_length][p_length]


