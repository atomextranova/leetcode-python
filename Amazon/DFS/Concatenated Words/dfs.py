class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        exist_set = set(words)
        result = []
        for word in words:
            if self.dfs(word, exist_set):
                result.append(word)
        return result

    def dfs(self, s, exist_set):

        if not s:
            return False

        # Key: start from 1, use i
        # start from 0 and use i + 1 failed in some case
        for i in range(1, len(s)):
            prefix = s[:i]
            suffix = s[i:]

            if prefix in exist_set:
                if suffix in exist_set:
                    return True

                if self.dfs(suffix, exist_set):
                    return True
        return False


sol = Solution()
result = sol.findAllConcatenatedWordsInADict(
    ["cat", "cats", "catsdogcats", "dog", "dogcatsdog",
     "hippopotamuses", "rat", "ratcatdogcat"])
print(result)