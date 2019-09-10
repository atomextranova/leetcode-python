class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s:
            return 0

        if k >= len(s):
            return len(s)

        char_to_count = {}
        longest = 0
        left = 0
        # Iterate from right
        for right in range(len(s)):
            char_to_count[s[right]] = char_to_count.get(s[right], 0) + 1
            # Check condition by moving left to get longest
            while len(char_to_count) > k and left <= right:
                char_to_count[s[left]] = char_to_count[s[left]] - 1
                if char_to_count[s[left]] == 0:
                    del char_to_count[s[left]]
                left += 1

            longest = max(right - left + 1, longest)

        return longest