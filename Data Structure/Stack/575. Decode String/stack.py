class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """

    # Edge case:
    # nested pattern
    # s = ""

    # O(n)
    def expressionExpand(self, s):
        # write your code here
        if not s:
            return ""

        stack = []
        cur_string = ""
        cur_num_str = ""

        for char in s:
            if char.isdigit():
                cur_num_str += char
                continue

            if char == "[":
                # Save non-repeat string,
                # then store repeat pattern in cur_string
                stack.append(cur_string)
                stack.append(int(cur_num_str))
                cur_num_str = ""
                cur_string = ""
                continue

            if char == "]":
                repeat = stack.pop()
                prev_string = stack.pop()
                cur_string = prev_string + cur_string * repeat
                continue

            cur_string += char

        return cur_string

