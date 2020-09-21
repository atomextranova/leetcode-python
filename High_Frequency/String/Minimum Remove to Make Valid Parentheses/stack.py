class Solution:
    # Scan through
    def minRemoveToMakeValid(self, s: str) -> str:
        stack_left = []
        s_list = []
        if not s:
            return s

        for i in range(len(s)):
            if s[i] == "(":
                stack_left.append(i)
                s_list.append("(")
            elif s[i] == ")":
                if len(stack_left) > 0:
                    s_list.append(")")
                else:
                    s_list.append("")
            else:
                s_list.append(s[i])

        for index in stack_left:
            s_list[index] = ""

        return "".join(s_list)