class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        longest = 0
        left = 0
        right = 0
        for n in range(len(s)):
            start, end, cur = self.find_longest_helper(s, n - 1, n + 1, 1)
            if cur > longest:
                longest = cur
                left = start
                right = end

            if n < len(s) - 1:
                if s[n] != s[n+1]:
                    continue
                start, end, cur = self.find_longest_helper(s, n-1, n+2, 2)
                if cur > longest:
                    longest = cur
                    left = start
                    right = end

        return s[left:right + 1]

    def find_longest_helper(self, s, start, end, count):

        if start >= 0 and end < len(s) and s[start] == s[end]:
            return self.find_longest_helper(s, start - 1, end + 1, count + 2)
        else:
            return start + 1, end - 1, count
        
sol = Solution()
sol.longestPalindrome("babad")