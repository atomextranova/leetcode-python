class Solution:

    # O(4^n/n^0.5) / O(branch factor * max depth)
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []

        temp_result = []
        result = []
        self.helper(n, n, temp_result, result)
        return result

    def helper(self, left, right, temp_result, result):
        if left == 0 and right == 0:
            result.append("".join(temp_result))

        if left > 0:
            temp_result.append("(")
            self.helper(left - 1, right, temp_result, result)
            temp_result.pop()

        if right > left:
            temp_result.append(")")
            self.helper(left, right - 1, temp_result, result)
            temp_result.pop()
