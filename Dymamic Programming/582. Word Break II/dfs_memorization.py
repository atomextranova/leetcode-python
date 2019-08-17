# 求所有方案 = DFS
# Memorization 剪枝

class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """

    def wordBreak(self, s, wordDict):
        # write your code here
        if not wordDict:
            return []

        max_length = 0
        memo = {}
        temp_result = []
        for word in wordDict:
            max_length = max(max_length, len(word))
        return self.dfs(s, wordDict, 0, memo, max_length, temp_result)

    def dfs(self, s, wordDict, start_index, memo, max_length, temp_result):

        if start_index in memo:
            return memo[start_index]

        if start_index == len(s):
            return []

        memo[start_index] = []

        for i in range(start_index + 1, len(s)):
            if i - start_index > max_length:
                break
            word = s[start_index:i]
            if word not in wordDict:
                continue
            sub_list = self.dfs(s, wordDict, i, memo, max_length, temp_result)
            for sub in sub_list:
                memo[start_index].append(word + " " + sub)
        # Consider the whole substring
        if s[start_index:] in wordDict:
            memo[start_index].append(s[start_index:])

        return memo[start_index]