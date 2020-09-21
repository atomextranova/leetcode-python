class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0:
            return [[]]

        result = [[1] * n for _ in range(n)]

        change = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        index_change = 0
        start = [0, 0]
        start_val = 0
        for i in range(n - 1, 0, -2):
            for j in range(4):
                for k in range(i):
                    start_val += 1
                    result[start[0]][start[1]] = start_val
                    start[0] += change[j][0]
                    start[1] += change[j][1]

            start[0] += 1
            start[1] += 1
        if n % 2 == 1:
            result[start[0]][start[1]] = start_val + 1
        return result


sol = Solution()
sol.generateMatrix(3)