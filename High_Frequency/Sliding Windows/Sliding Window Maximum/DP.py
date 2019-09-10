class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums

        length = len(nums)
        left_array = [0] * length
        right_array = [0] * length

        left_array[0] = nums[0]
        right_array[length - 1] = nums[length - 1]

        for left in range(1, length):
            right = length - left - 1
            # left = max element from block start to left
            if left % k == 0:
                left_array[left] = nums[left]
            else:
                left_array[left] = max(nums[left], left_array[left - 1])

            # right = max element from block end to right
            if (right + 1) % k == 0:
                right_array[right] = nums[right]
            else:
                right_array[right] = max(nums[right], right_array[right + 1])

        length_result = length - k + 1
        result = [0] * length_result
        for i in range(length_result):
            result[i] = max(right_array[i], left_array[i + k - 1])
        return result
