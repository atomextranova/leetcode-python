class Solution:
    """
    @param s: a string
    @return: an integer
    """

    # Two pointers
    # Fix slow, move fast to get longest for slow in range(length)

    # O(n)

    def lengthOfLongestSubstring(self, s):
        # write your code here

        if not s:
            return 0

        unique_set = set()
        fast = 0
        longest_length = 0
        for slow in range(len(s)):
            while fast < len(s) and s[fast] not in unique_set:
                unique_set.add(s[fast])
                fast += 1

            longest_length = max(longest_length, fast - slow)
            unique_set.remove(s[slow])

        return longest_length