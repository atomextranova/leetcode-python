class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordSet):
        # write your code here
        if not s:
            return []

        if not wordSet:
            return []

        memo = dict()
        min_length = float('inf')
        max_length = float('-inf')
        for word in wordSet:
            length = len(word)
            min_length = min(min_length, length)
            max_length = max(max_length, length)
        result = self.dfs(s, wordSet, memo, min_length, max_length)
        return result

    def dfs(self, s, wordSet, memo, min_length, max_length):
        if s in memo:
            return memo[s]

        if not s:
            return [""]

        memo[s] = []
        cur_length = len(s)
        for i in range(min_length, max_length + 1):
            # Avoid index error
            # for "de", s[:2], s[:3]... will all get "de""
            if i > cur_length:
                break
            word = s[:i]
            if word in wordSet:
                suffixes = self.dfs(s[i:], wordSet, memo, min_length, max_length)
                result = [word + " " + suffix if suffix else word for suffix in suffixes]
                memo[s].extend(result)

        return memo[s]
