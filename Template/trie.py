class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    # Continuously construct node for each char in word
    # set the final node to be true
    def insert(self, word):
        # write your code here
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_word = True

    # Helper function
    # return the node for word's final char or none
    def find(self, word):
        node = self.root
        for char in word:
            node = node.children.get(char, None)
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

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """

    def startsWith(self, prefix):
        # write your code here
        return self.find(prefix) is not None
