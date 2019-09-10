class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums

        if len(nums) == 1:
            return nums

        end = len(nums) - 1
        # Find first element < its successor
        # whose index is end - 1
        while end > 0:
            # Only break only if >
            # E.g. [5,1,1] -> [1,1,5]
            if nums[end] > nums[end - 1]:
                break
            end -= 1

        # The array is in descending order
        # Reverse: [5, 2, 1] -> [1,2,5]
        if end == 0:
            return nums.reverse()

        # From end, find the first element larger than found
        # pivot
        for i in range(len(nums) - 1, end - 1, -1):
            if nums[i] > nums[end - 1]:
                nums[i], nums[end - 1] = nums[end - 1], nums[i]
                break
        # nums[a:b] = nums[a:b][::-1]
        # Reverse the rest of array
        for i in range(end, (end + len(nums)) // 2):
            nums[i], nums[len(nums) - i - 1 + end] = nums[len(
                nums) - i - 1 + end], nums[i]
        return nums