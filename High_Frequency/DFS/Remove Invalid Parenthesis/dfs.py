class Solution:
    def removeInvalidParentheses(self, s: str):
        # count unmatched
        left_wrong = 0
        right_wrong = 0
        for char in s:
            if char == "(":
                left_wrong += 1
            elif char == ")":
                if left_wrong > 0:
                    left_wrong -= 1
                else:
                    right_wrong += 1
        # set to avoid duplicates
        result = set()

        self.dfs(s, left_wrong, right_wrong, 0, 0, 0, "", result)

        return list(result)

    def dfs(self, s, left_remove, right_remove, left_count, right_count,
            cur_index, temp_result, result):
        # Recursion until end
        # left_remove and right_remove == 0 does not guarantee correct
        # ")()(" -> ")(" still wrong. keep checking the rest
        if left_remove == 0 and right_remove == 0 and cur_index == len(s):
            result.add(temp_result + s[cur_index:])
            return

        if cur_index == len(s):
            return

        char = s[cur_index]
        if char == "(":
            if left_remove > 0:
                self.dfs(s, left_remove - 1, right_remove, left_count,
                         right_count, cur_index + 1, temp_result,
                         result)
            self.dfs(s, left_remove, right_remove, left_count + 1,
                     right_count, cur_index + 1, temp_result + char,
                     result)

        elif char == ")":
            if right_remove > 0:
                self.dfs(s, left_remove, right_remove - 1, left_count,
                         right_count, cur_index + 1,
                         temp_result, result)
            # only add if left has unmatched
            if left_count > right_count:
                self.dfs(s, left_remove, right_remove, left_count ,
                             right_count+1, cur_index + 1,
                             temp_result + char, result)
        else:
            # adding non parentheses
            self.dfs(s, left_remove, right_remove, left_count, right_count,
                cur_index+1, temp_result+char, result)
