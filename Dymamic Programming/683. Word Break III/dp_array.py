# 时间复杂度 O(nL^ 2)
# 其中n为s长度， L为dict里面最长单词长度。总共 n个答案，因此时间复杂度 O(nL^ 2)
# 空间复杂度 O(n)（额外空间）

class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # Write your code here
        if not dict:
            return 0
        length = len(s)
        word_count = [0] * (length + 1)
        word_count[0] = 1
        max_length = 0
        lower_dict = set()
        for word in dict:
            lower_dict.add(word.lower())
        for word in dict:
            max_length = max(max_length, len(word))
        for i in range(1, length + 1):
            for j in range(1, min(i, max_length) + 1):
                word = s[i - j:i].lower()
                if word in lower_dict:
                    word_count[i] += word_count[i - j]

        return word_count[length]
