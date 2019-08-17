# recursion + memoization
# 如果用记忆化搜索的缺陷，递归深度太深，导致 StackOverflow
# 时间复杂度 O(nL^ 2)
# 空间复杂度 O(n) （memo存储 n种不同可能）
# 其中n为s长度， L为dict里面最长单词长度。

# StackOverflow

class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, dict):
        # write your code here
        max_length = 0
        memo = {}
        for word in dict:
            max_length = max(max_length, len(word))
        return self.dfs(s, dict, 0, memo, max_length)

    def dfs(self, s, dict, start_index, memo, max_length):
        if start_index in memo:
            return memo[start_index]

        if start_index == len(s):
            return True

        memo[start_index] = False
        for i in range(start_index + 1, len(s) + 1):
            if i - start_index > max_length:
                break
            word = s[start_index:i]
            if word not in dict:
                continue
            memo[start_index] = self.dfs(s, dict, i, memo, max_length)
            if memo[start_index]:
                return memo[start_index]

        return memo[start_index]



