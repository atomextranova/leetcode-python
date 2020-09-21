class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = set(wordDict)
        return self.helper(s, memo)

    # Key TLE Factor: Did not store false result
    def helper(self, s, memo):
        if s == "":
            return True

        if s in memo:
            return True

        for i in range(len(s)):
            prefix = s[:i + 1]
            if prefix not in memo:
                continue

            suffix = s[i + 1:]
            if suffix in memo:
                memo.add(s)
                return True

            if self.helper(suffix, memo):
                memo.add(suffix)
                memo.add(s)
                return True

        return False