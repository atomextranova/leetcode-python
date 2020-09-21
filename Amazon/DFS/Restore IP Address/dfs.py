class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        result = []
        self.dfs(s, 0, result, [])
        return result

    def dfs(self, s, index, result, temp_result):
        # Stop first when index reach 4
        if index == 4:
            # print(temp_result)
            # # print(s)
            # Check used up
            if not s:
                result.append(".".join(temp_result))
            return

        for i in range(1, 4):
            # Check for valid s[:i]
            if i > len(s):
                break
            cur_str = s[:i]
            cur_num = int(s[:i])
            # Check for > 255 or sequence like 00/03
            if cur_num > 255 or (str(cur_num) != cur_str):
                break
            # Backtrack
            temp_result.append(cur_str)
            self.dfs(s[i:], index + 1, result, temp_result)
            temp_result.pop()
