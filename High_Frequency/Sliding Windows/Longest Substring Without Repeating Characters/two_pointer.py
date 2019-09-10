class Solution:
    # Edge case:
    # not s -> 0
    # " " -> 1
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_to_index = {}
        longest = 1
        left = -1

        for right in range(len(s)):
            # left = 当前character上次occurrence，所有之前character最近的occurrence
            left = max(char_to_index.get(s[right], -1), left)
            longest = max(longest, right - left)
            char_to_index[s[right]] = right

        return longest