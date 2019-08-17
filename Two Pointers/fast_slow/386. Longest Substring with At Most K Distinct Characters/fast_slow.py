class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    # Edge case:
    # k = 0
    # s = ""

    # Two pointers

    # O(n)

    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if not s or k == 0:
            return 0

        unique_dict = {}
        fast = 0
        longest_length = 0
        for slow in range(len(s)):
            while fast < len(s):
                if s[fast] not in unique_dict:
                    if len(unique_dict) == k:
                        break
                    else:
                        unique_dict[s[fast]] = 1
                else:
                    unique_dict[s[fast]] += 1
                fast += 1

            longest_length = max(longest_length, fast - slow)
            if unique_dict[s[slow]] == 1:
                del unique_dict[s[slow]]
            else:
                unique_dict[s[slow]] -= 1

        return longest_length