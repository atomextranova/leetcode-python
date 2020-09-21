class TrieNode:

    def __init__(self):
        self.is_word = False
        self.char_to_dict = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            return
        node = self.root
        for char in word:
            if char not in node.char_to_dict:
                node.char_to_dict[char] = TrieNode()
            node = node.char_to_dict[char]
        node.is_word = True

    def get_end_word(self):
        result = []
        queue = [(self.root, "")]
        while queue:
            node, cur_str = queue.pop()
            if len(node.char_to_dict) != 0:
                for char, node in node.char_to_dict.items():
                    new_str = cur_str + char
                    queue.append((node, new_str))
            else:
                result.append(cur_str)
        return result

    # Helper function
    # return the node for word's final char or none
    def find(self, word):
        node = self.root
        for char in word:
            node = node.char_to_dict.get(char, None)
            if node is None:
                return None
        return node

    """
    @param: word: A string
    @return: if the word is in the trie.
    """

    def search(self, word):
        # write your code here
        node = self.find(word)
        return node is not None and node.is_word


class Solution:

    def findAllConcatenatedWordsInADict(self, words):
        trie = Trie()
        self.memo = {}
        for word in words:
            trie.insert(word)

        # temp_results = trie.get_end_word()
        results = []
        for word in words:
            if self.dfs(trie, word, 0, 0, len(word)):
                results.append(word)
        print(self.memo)
        return results

    def dfs(self, trie, word, start, count, length):
        if start == length:
            return count > 1

        sub_word = word[start:]
        if sub_word in self.memo:
            return self.memo[sub_word]

        for i in range(start, length):
            sub_word = word[start:i + 1]

            if trie.search(sub_word):
                if self.dfs(trie, word, i + 1, count + 1, length):
                    self.memo[sub_word] = True
                    return True
            else:
                continue
            # print(word, count, start)
            # if count > 1 and start == len(result):
            #     results.append(result)
        self.memo[sub_word] = False
        return False

sol = Solution()
print(sol.findAllConcatenatedWordsInADict(["a","b","ab","abc"]))