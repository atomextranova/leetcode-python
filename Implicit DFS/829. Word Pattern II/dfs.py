#
# 829. Word Pattern II
# 中文English
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty substring in str.(i.e if a corresponds to
# s, then b cannot correspond to s. For example, given pattern = "ab",
# str = "ss", return false.)
#
# Example
# Example 1
#
# Input:
# pattern = "abab"
# str = "redblueredblue"
# Output: true
# Explanation: "a"->"red","b"->"blue"
# Example 2
#
# Input:
# pattern = "aaaa"
# str = "asdasdasdasd"
# Output: true
# Explanation: "a"->"asd"
# Example 3
#
# Input:
# pattern = "aabb"
# str = "xyzabcxzyabc"
# Output: false
# Notice
# You may assume both pattern and str contains only lowercase letters.

class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """

    def wordPatternMatch(self, pattern, str):
        # write your code here
        return self.match(pattern, str, {}, set())

    def match(self, pattern, string, mapping, used):
        if not pattern:
            return not string

        char = pattern[0]
        if char not in mapping:
            for i in range(len(string)):
                temp_word = string[:i + 1]
                if temp_word in used:
                    continue
                mapping[char] = temp_word
                used.add(temp_word)
                if self.match(pattern[1:], string[i + 1:], mapping, used):
                    return True
                del mapping[char]
                used.remove(temp_word)
            return False

        if char in mapping:
            temp_word = mapping[char]
            length = len(temp_word)
            if not string.startswith(temp_word):
                return False
            return self.match(pattern[1:], string[length:], mapping, used)