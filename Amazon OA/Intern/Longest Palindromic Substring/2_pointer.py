class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """

    def longestPalindrome(self, s):
        if not s:
            return 0
        # write your code here
        longest = 0
        left = 0
        right = 0
        for i in range(len(s)):
            l, r, length = self.helper(s, i, i)
            if longest < length:
                left = l
                right = r
                longest = length
            l1, r1, length1 = self.helper(s, i, i + 1)
            if longest < length1:
                left = l1
                right = r1
                longest = length1

        return s[left:right + 1]

    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - 1, right - left - 1
