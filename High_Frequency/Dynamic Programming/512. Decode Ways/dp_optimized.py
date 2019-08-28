class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """

    def numDecodings(self, s):
        # write your code here

        # Empty s
        if not s:
            return 0

        if s[0] == "0":
            return 0

        # len = 1
        length = len(s)
        if length == 1:
            return 1

        # sliding array to optimize space
        dp_table = [0] * (3)
        dp_table[0] = 1

        # include 26
        # get rid of 0 case, like 20, only has 1 possiblity
        if 10 <= int(s[:2]) <= 26 and s[1] != "0":
            dp_table[1] = 2
        else:
            dp_table[1] = 1

        for i in range(2, length):
            # 00 -> not possible to any
            if s[i] == "0" and s[i - 1] == "0":
                return 0
            # Optimized require cleanup history
            dp_table[i % 3] = 0

            # current char = 0 -> must cobine with previous char
            # -> dp[i-1] not possible, which is only valid
            # if i-1 stand by itself

            if s[i] != "0":
                dp_table[i % 3] += dp_table[(i - 1) % 3]
                # Inclusive on both sides
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                dp_table[i % 3] += dp_table[(i - 2) % 3]

        return dp_table[(length - 1) % 3]