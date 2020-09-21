from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        if (beginWord == endWord):
            return 0

        if endWord not in wordList:
            return 0

        start_queue = deque([beginWord])
        end_queue = deque([endWord])
        startword_to_distance = {}
        endword_to_distance = {}
        distance = 0
        while start_queue and end_queue:
            for i in range(len(start_queue)):
                cur_word = start_queue.popleft()
                startword_to_distance[cur_word] = distance
                next_words = self.next_word(cur_word, wordList,
                                            startword_to_distance, distance + 1)
                for next_word in next_words:
                    if next_word in endword_to_distance:
                        return (distance + 1) + endword_to_distance[
                            next_word] + 1
                    start_queue.append(next_word)

            for i in range(len(end_queue)):
                cur_word = end_queue.popleft()
                endword_to_distance[cur_word] = distance
                next_words = self.next_word(cur_word, wordList,
                                            endword_to_distance, distance + 1)
                for next_word in next_words:
                    if next_word in startword_to_distance:
                        return (distance + 1) + startword_to_distance[
                            next_word] + 1
                    end_queue.append(next_word)

            distance += 1

        return 0

    def next_word(self, word, wordList, word_to_distance, distance):
        result = []
        for i in range(len(word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                temp_word = word[:i] + char + word[i + 1:]
                if temp_word in wordList and temp_word not in word_to_distance:
                    result.append(temp_word)
                    word_to_distance[temp_word] = distance

        return result


sol = Solution()
print(sol.ladderLength(
    "red",
"tax",
["ted","tex","red","tax","tad","den","rex","pee"]))
