class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """

    def anagram(self, s, t):
        # write your code here
        # both emtpy
        if not s and not t:
            return True
        # one empty
        if not s or not t:
            return False

        # Could use [0] * 26
        char_dict = {}
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

        for char in t:
            if char not in char_dict:
                return False
            else:
                char_dict[char] -= 1

        for count in char_dict.values():
            if count != 0:
                return False

        return True
