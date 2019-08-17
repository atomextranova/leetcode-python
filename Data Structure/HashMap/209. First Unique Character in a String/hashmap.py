

class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """

    def firstUniqChar(self, str):
        # Write your code here
        char_to_count = {}
        for char in str:
            if char in char_to_count:
                char_to_count[char] += 1
            else:
                char_to_count[char] = 1

        for char in str:
            if char_to_count[char] == 1:
                return char