class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        return self.helper(s, 0, len(s) - 1, False)

    def helper(self, s, left, right, deleted):
        # < / <= both works
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue

            if deleted:
                return False

            deleted = True
            return self.helper(s, left + 1, right, deleted) \
                   or self.helper(s, left, right - 1, deleted)

        return True


sol = Solution()
sol.validPalindrome("aba")