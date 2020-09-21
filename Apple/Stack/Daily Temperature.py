class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        stack = []
        for i in range(len(T) - 1, -1, -1):
            t = T[i]
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()

            if stack:
                result[i] = stack[-1] - i
            stack.append(i)

        return result