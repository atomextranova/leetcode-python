class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """

    def kDistinctCharacters(self, s, k):
        # Write your code here
        if len(s) < k:
            return 0

        cur_chars = dict()

        left = 0
        right = 0
        total = 0

        for right in range(len(s)):
            cur_char = s[right]
            cur_chars[cur_char] = cur_chars.get(cur_char, 0) + 1
            while len(cur_chars) >= k:
                cur_chars[s[left]] -= 1

                if cur_chars[s[left]] == 0:
                    del cur_chars[s[left]]

                left += 1

            total += left

        return total