class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordSet):
        # write your code here
        if not s:
            return True

        if not wordSet:
            return False

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
        for i in range(min_length, max_length + 1):
            if i > len(s):
                break
            word = s[:i]
            if word in wordSet:
                suffixes = self.dfs(s[i:], wordSet, memo, min_length, max_length)
                print(suffixes)
                result = [word + " " + suffix if suffix else word for suffix in suffixes]
                print(memo)
                memo[s].extend(result)

        return memo[s]

sol = Solution()
print(sol.wordBreak("lintcode", ["de","ding","co","code","lint"]))