class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, wordSet):
        if not s:
            return 0

        if not wordSet:
            return 0

        s = s.lower()
        wordSet = set([word.lower() for word in wordSet])

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
            return 1

        memo[s] = 0
        cur_length = len(s)
        for i in range(min_length, max_length + 1):
            # Avoid index error
            # for "de", s[:2], s[:3]... will all get "de""
            if i > cur_length:
                break
            word = s[:i]
            if word in wordSet:
                memo[s] += self.dfs(s[i:], wordSet, memo, min_length, max_length)

        return memo[s]