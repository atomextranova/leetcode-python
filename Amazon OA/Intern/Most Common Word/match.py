from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if not paragraph:
            return []
        word_count = defaultdict(int)
        word = ""
        banned = set(banned)
        max_val = 0
        max_word = ""
        for i, char in enumerate(paragraph.lower() + " "):
            if char == " " or not char.isalpha():
                if word not in banned and word != "":
                    word_count[word] += 1
                    if word_count[word] > max_val:
                        max_val = word_count[word]
                        max_word = word
                word = ""
                continue
            word += char
        return max_word