class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """

    # Edge case:
    # nested pattern
    # s = ""

    def expressionExpand(self, s):
        # write your code here
        if not s:
            return ""

        result, _ = self.dfs_helper(s, 0, len(s), 0)
        return result

    def dfs_helper(self, s, start_index, length, cur_num):
        # return start_index to match output, not useful here
        if start_index == length:
            return "", start_index

        cur_string = ""
        while start_index < length:
            cur_char = s[start_index]

            # sub problem: find the repeat pattern and
            # continue scanning the rest
            if cur_char == "[":
                repeat_pattern, start_index = self.dfs_helper(s,
                                                              start_index + 1,
                                                              length, 0)
                cur_string += repeat_pattern * cur_num
                cur_num = 0
                continue

            # tell the where to stop
            if cur_char == "]":
                return cur_string, start_index + 1

            # Count the repeat factor for repeating pattern
            if cur_char.isdigit():
                cur_num = cur_num * 10 + int(cur_char)
                start_index += 1
                continue

            # Push char to current string normally
            cur_string += cur_char
            start_index += 1

        return cur_string, start_index






