# Approach 1:
# Sort all Strings, use dictionary to count the same strings
# append index to the dictionary
# if count >= 2, extend strs[index] for all index of current anagram

from collections import defaultdict


class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """

    def anagrams(self, strs):
        # write your code here
        if not strs:
            return []

        result = []
        temp_strs = [""] * len(strs)
        for i in range(len(strs)):
            temp_strs[i] = ''.join(sorted(strs[i]))

        count = defaultdict(list)
        for i, s in enumerate(temp_strs):
            count[s].append(i)

        for s, indexes in count.items():
            if len(indexes) >= 2:
                for index in indexes:
                    result.append(strs[index])

        return result