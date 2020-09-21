class Solution:
    # Key: store prev_num / prev_op
    # When encounter a new number, calculate results of
    # prev_num and prev_op, store result in prev_num
    # Add result in loop if prev_op in "+-"
    # Add the result at the final step
    # Default prev_op = +
    # for prev_num // cur_num < 0 and prev_num % cur_num != 0
    # +1 to truncate towards 0
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        result = 0
        prev_num = 0
        prev_op = "+"
        i = 0
        while i < len(s):
            char = s[i]
            if char == " ":
                i += 1
                continue

            if char in "+-*/":
                prev_op = char
                i += 1
                continue

            if char.isdigit():
                cur_num = int(char)
                while i + 1 < len(s) and s[i + 1].isdigit():
                    cur_num = cur_num * 10 + int(s[i + 1])
                    i += 1
                i += 1
                if prev_op == "+":
                    result += prev_num
                    prev_num = cur_num
                if prev_op == "-":
                    result += prev_num
                    prev_num = -cur_num
                if prev_op == "*":
                    prev_num = cur_num * prev_num
                if prev_op == "/":
                    if prev_num < 0 and prev_num % cur_num != 0:
                        prev_num = prev_num // cur_num + 1
                    else:
                        prev_num = prev_num // cur_num

        result += prev_num
        return result


