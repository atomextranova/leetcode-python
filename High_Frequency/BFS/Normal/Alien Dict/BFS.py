from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    # 1. 统计出现字符
    # 2. 比较以得出前后关系，用dict of set, set 装word order在他之后
    # 3.Topological Sort
    # 3.1.construct in_degree
    # 3.2.每次remove in_degree为0，update
    # 4. 检查结果是否包含所有字符

    # Edge case
    # if len(word1) > len(word2)
    # ["z", "z"]
    # ["ab","adc"]
    def alienOrder(self, words: List[str]) -> str:
        char_to_successor = defaultdict(set)

        for word in words:
            for char in word:
                if char not in char_to_successor:
                    char_to_successor[char] = set()
        # Last word do not have any succesor
        # No need to compare
        for i in range(len(words) - 1):
            word = words[i]
            next_word = words[i + 1]
            # guaranteed that len(word) > len(next_word)
            # if word is a prefix of next_word
            for j in range(len(word)):
                # Put here to deal with case like ["z","z"]
                # print(word[j], next_word[j])
                if word[j] == next_word[j]:
                    continue
                char_to_successor[word[j]].add(next_word[j])

                break

        in_degree_dict = defaultdict(int)
        # If use heap, get the smallest lexicographical order
        # If list, decided by the input
        heap = []

        # Build in_degree map
        for char, next_set in char_to_successor.items():
            if char not in in_degree_dict:
                in_degree_dict[char] = 0
            for next_char in next_set:
                in_degree_dict[next_char] += 1

        for char, in_degree in in_degree_dict.items():
            if in_degree == 0:
                heappush(heap, char)

        result = []
        # Topological sort process
        while len(heap) > 0:
            char = heappop(heap)
            for next_char in char_to_successor[char]:
                in_degree_dict[next_char] -= 1
                if in_degree_dict[next_char] == 0:
                    heappush(heap, next_char)
            result.append(char)

        # If not fully topological sorted
        if len(result) != len(char_to_successor):
            return ""

        return "".join(result)
