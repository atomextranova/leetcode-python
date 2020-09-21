import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return t

        if not s:
            return s

        # count everything in t
        pattern = {}
        for char in t:
            pattern[char] = pattern.get(char, 0) + 1

        char_to_count = {}

        matched = 0
        left_index = 0
        right_index = -1
        length_result = sys.maxsize
        left = 0
        right = 0
        while right < len(s):
            char = s[right]
            # Not in t -> ignore
            if char not in pattern:
                right += 1
                continue
            # char += 1, check match
            char_to_count[char] = char_to_count.get(char, 0) + 1
            if char_to_count[char] == pattern.get(char):
                matched += 1

            while left <= right and matched == len(pattern):
                # Only change if result improves
                if right - left + 1 < length_result:
                    length_result = right - left + 1
                    left_index = left
                    right_index = right

                char = s[left]
                if char not in pattern:
                    left += 1
                    continue
                # If remove char cause matched decrease
                char_to_count[char] = char_to_count.get(char) - 1
                if char in pattern and char_to_count[char] < pattern[char]:
                    matched -= 1
                left += 1
            right += 1

        if length_result == sys.maxsize:
            return ""
        return s[left_index:right_index + 1]