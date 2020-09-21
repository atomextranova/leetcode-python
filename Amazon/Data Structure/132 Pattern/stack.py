from typing import List


class Solution:

    # Use a list to store min_num up to this point
    # min_num stands for 1
    # Use a stack to track numbers > current min_num, from right to left
    # stack pops any <= cur min_num
    # if num[i] > stack[-1], num[i] is 3
    # pattern found
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums:
            return False

        if len(nums) < 3:
            return False

        min_num = [0] * len(nums)
        min_num[0] = nums[0]
        for i in range(1, len(nums)):
            min_num[i] = min(min_num[i - 1], nums[i])

        stack = []

        for i in range(len(nums) - 1, 0, -1):
            while (len(stack) != 0 and stack[-1] <= min_num[i]):
                stack.pop()

            if (len(stack) != 0 and stack[-1] < nums[i]):
                return True

            stack.append(nums[i])

        return False
