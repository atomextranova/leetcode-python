class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        temp = []
        result = []
        self.dfs(n, n, temp, result)
        return result

    def dfs(self, left, right, temp, result):
        if left < 0 or right < 0:
            return

        if left == right == 0:
            result.append("".join(temp))
            return

        temp.append("(")
        self.dfs(left - 1, right, temp, result)
        temp.pop()

        if left < right:
            temp.append(")")
            self.dfs(left, right - 1, temp, result)
            temp.pop()
