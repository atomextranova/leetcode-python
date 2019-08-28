class ValidWordAbbr:
    """
    @param: dictionary: a list of words
    """

    def __init__(self, dictionary):
        # do intialization if necessary
        self.word_to_dict = {}
        for orig_word in dictionary:
            word = self.get_abbr(orig_word)
            if word not in self.word_to_dict:
                self.word_to_dict[word] = set()
            self.word_to_dict[word].add(orig_word)

    """
    @param: word: a string
    @return: true if its abbreviation is unique or false
    """

    def isUnique(self, word):
        # write your code here
        abbr = self.get_abbr(word)
        if abbr not in self.word_to_dict:
            return True
        word_list = self.word_to_dict[abbr]
        return word in word_list and len(word_list) == 1

    def get_abbr(self, word):
        if len(word) < 2:
            return word
        else:
            return word[0] + str(len(word) - 2) + word[-1]

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param = obj.isUnique(word)