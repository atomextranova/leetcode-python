class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """

    # Scan through word and abbr
    # If abbr[i] is char
    # check word[j] == abbr[i], i+1 and j+1 if true
    # if abbr[i] is digit
    # if == 0: return False
    # if != 0, extract number, skip word through chars
    def validWordAbbreviation(self, word, abbr):
        # write your code here
        if not abbr:
            return False

        word_index = 0
        abbr_index = 0
        while word_index < len(word) and abbr_index < len(abbr):
            num = 0
            char = word[word_index]
            c = abbr[abbr_index]
            if c.isdigit():
                if int(c) == 0:
                    return False
                temp = abbr_index
                while temp < len(abbr) and abbr[temp].isdigit():
                    temp += 1
                if temp > abbr_index:
                    num = int(abbr[abbr_index:temp])
                word_index += num
                abbr_index = temp
                continue

            if char != c:
                break

            abbr_index += 1
            word_index += 1
            # print(word_index, abbr_index)

        return word_index == len(word) and abbr_index == len(abbr)