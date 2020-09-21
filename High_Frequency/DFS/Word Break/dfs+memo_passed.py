class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = {key: True for key in wordDict}
        return self.helper(s, memo)

    # Will still fail on lintcode for large cases
    def helper(self, s, memo):
        if s == "":
            return True

        if s in memo:
            return memo[s]

        memo[s] = False

        for i in range(len(s)):
            prefix = s[:i + 1]
            if prefix not in memo or not memo[prefix]:
                continue

            suffix = s[i + 1:]

            memo[s] = self.helper(suffix, memo)
            if memo[s]:
                return memo[s]

        return memo[s]