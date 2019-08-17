KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):
        # write your code here
        if not digits:
            return []

        results = []
        temp_results = []
        # Ordered
        self.dfs(results, temp_results, digits, 0,
                 len(digits), '')
        return results

    def dfs(self, results, temp_results, digits, start_index, length, cur_str):
        characters = KEYBOARD[digits[start_index]]
        for i in range(len(characters)):
            temp_str = cur_str + characters[i]
            if start_index == length - 1:
                results.append(temp_str)
            else:
                self.dfs(results, temp_results, digits, start_index + 1, length, temp_str)