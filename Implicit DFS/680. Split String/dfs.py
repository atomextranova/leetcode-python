# 680. Split String
# 中文English
# Give a string, you can choose to split the string after one character or two adjacent characters, and make the string to be composed of only one character or two characters. Output all possible results.
#
# Example
# Example1
#
# Input: "123"
# Output: [["1","2","3"],["12","3"],["1","23"]]
# Example2
#
# Input: "12345"
# Output: [["1","23","45"],["12","3","45"],["12","34","5"],["1","2","3","45"],["1","2","34","5"],["1","23","4","5"],["12","3","4","5"],["1","2","3","4","5"]]

class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        result = []
        self.dfs(result, [], s, 0, len(s))
        return result

    def dfs(self, result, temp_result, s, i, length):

        if i == length:
            result.append(list(temp_result))

        for j in range(2):
            if i + j < length:
                temp_result.append(s[i:i + j + 1])
                self.dfs(result, temp_result, s, i + j + 1, length)
                temp_result.pop()
