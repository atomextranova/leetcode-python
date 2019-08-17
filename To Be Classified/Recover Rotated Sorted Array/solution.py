class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """

    def recoverRotatedSortedArray(self, nums):
        # write your code here
        start_index = 0
        length = len(nums)
        current = nums[start_index]
        while start_index < length:

            next_element = nums[start_index+1]

            if current > next_element:
                break
            else:
                start_index += 1
                current = next_element

        nums[0:start_index+1] = nums[start_index::-1]
        nums[start_index+1:] = nums[-1:start_index:-1]

        nums = nums[::-1]

        return nums

sol = Solution()
print(sol.recoverRotatedSortedArray([4, 5, 1, 2, 3]))