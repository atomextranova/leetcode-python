from collections import defaultdict


class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    # window: end ~ start
    # window length: (end - start + 1)
    # Max count: among all seen window, the largest count of a character
    # Update start when: valid window length - max_count > k (Too large,
    # can only change k char when at least k + 1 char need to be changed)
    # Valid window length: after update start, the window is valid
    # result = max(all valid window length)
    def characterReplacement(self, s, k):
        # write your code here
        count_character = defaultdict(int)
        start = 0
        max_count = 0
        result = 0
        for end in range(len(s)):
            cur_char = s[end]
            count_character[cur_char] += 1
            max_count = max(max_count, count_character[cur_char])
            cur_length = end - start + 1
            if cur_length - max_count > k:
                count_character[s[start]] -= 1
                start += 1
                cur_length -= 1
            result = max(result, cur_length)
        return result
