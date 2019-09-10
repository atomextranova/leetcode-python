from collections import defaultdict


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not order or not words:
            return True

        index = 0
        self.char_to_order = defaultdict(int)
        for char in order:
            self.char_to_order[char] = index
            index += 1

        last_word = words[0]
        for i in range(len(words)):
            cur_word = words[i]
            if not self.correctly_sorted(last_word, cur_word):
                return False
            last_word = cur_word
        return True

    def correctly_sorted(self, word1, word2):
        for i in range(min(len(word1), len(word2))):

            if self.char_to_order[word1[i]] < self.char_to_order[word2[i]]:
                return True
            if self.char_to_order[word1[i]] > self.char_to_order[word2[i]]:
                return False

        return len(word1) <= len(word2)