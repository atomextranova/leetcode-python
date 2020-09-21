class Solution:
    """
    @param steps: steps you can move
    @param arrLen: the length of the array
    @return: Number of Ways to Stay in the Same Place After Some Steps
    """
    def numWays(self, steps, arrLen):
        # write your code here

        return self.numWaysHelper(steps, arrLen, 0) % 10000007

    def numWaysHelper(self, steps, arrLen, cur_index):
        if cur_index < 0 or cur_index >= arrLen:
            return 0
        if steps == 1:
            if cur_index == 0:
                return 0
            else:
                return 1
        if steps < cur_index:
            return 0

        nextSteps = steps - 1
        return self.numWaysHelper(nextSteps, arrLen, cur_index - 1) + \
               self.numWaysHelper(nextSteps, arrLen, cur_index) + \
               self.numWaysHelper(nextSteps, arrLen, cur_index + 1)

sol = Solution()
print(sol.numWays(3, 2))