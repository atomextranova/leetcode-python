class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()

    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """

    def addWord(self, word):
        # write your code here
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_word = True

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """

    def search(self, word):
        # write your code here
        if not word:
            return False

        return self.search_helper(word, 0, self.root)

    def search_helper(self, word, index, node):
        if len(word) == index:
            return node.is_word

        char = word[index]

        if char == ".":
            found = False
            for child in node.children.values():
                found = found or self.search_helper(word, index + 1, child)
            return found

        child = node.children.get(char, None)
        if child is None:
            return False

        return self.search_helper(word, index + 1, child)

sol = WordDictionary()
sol.addWord("a")
print(sol.search("."))


