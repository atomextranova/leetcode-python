class Solution:
    """
    @param steps: steps you can move
    @param arrLen: the length of the array
    @return: Number of Ways to Stay in the Same Place After Some Steps
    """
    def numWays(self, steps, arrLen):
        # write your code here
        old_array = [0] * (arrLen + 2)
        new_array = [0] * (arrLen + 2)
        old_array[1] = 1
        for i in range(steps):
            for j in range(1, min(arrLen + 1, steps + 1)):
                new_array[j] += old_array[j-1] + old_array[j] + old_array[j+1]
            old_array = new_array
            new_array = [0] * (arrLen + 2)

        return old_array[1] % (10000007)
sol = Solution()
sol.numWays(10, 3)
