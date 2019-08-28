class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """

    # Edge case
    # Empty word -> not allowed in problem
    # Empty abbr -> False
    # 0 -> False
    # Abbr length > word length
    # Abbr end with number -> = length -> True, else False
    def validWordAbbreviation(self, word, abbr):
        # write your code here
        if not abbr:
            return False

        word_index = 0
        cur_digit = 0
        for char in abbr:
            if char.isalpha():
                # Skip index and clear count of abbr
                if cur_digit != 0:
                    word_index += cur_digit
                    cur_digit = 0
                # Avoid index error, and return false
                if word_index > len(word):
                    return False
                # Check char match
                if word[word_index] != char:
                    return False
                word_index += 1

            if char.isdigit():
                # Trailing 0 (Leading 0 case), like 01
                if char == "0" and cur_digit == 0:
                    return False
                cur_digit = cur_digit * 10 + int(char)

        if cur_digit > 0:
            word_index += cur_digit
            # If word_index == length -> matched exactly, < -> not enough abbr,
            # > ->
            return word_index == len(word)

        return True

