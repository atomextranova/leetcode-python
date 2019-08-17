class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or s == s[::-1]:
            return s

        length = len(s)
        palindrome_table = [[False] * length for _ in range(length)]
        for i in range(length):
            palindrome_table[i][i] = True

        # When reach here, length of palindrome is >= 2
        longest_length = 1
        left, right = 0, 0
        # look for length >= 2
        for possible_length in range(2, length):
            for candidate_start_index in range(length - possible_length + 1):
                candidate_end_index = candidate_start_index + possible_length - 1
                # key
                is_palindrome = s[candidate_start_index] == s[candidate_end_index]
                if possible_length > 2:
                    is_palindrome = is_palindrome and palindrome_table[candidate_start_index + 1][
                        candidate_end_index - 1]
                palindrome_table[candidate_start_index][candidate_end_index] = is_palindrome
                if is_palindrome and possible_length > longest_length:
                    # memorize index instead of string
                    left, right = candidate_start_index, candidate_end_index
        return s[left:right + 1]
