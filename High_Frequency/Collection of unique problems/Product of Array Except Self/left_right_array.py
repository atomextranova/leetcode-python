class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        result = [0] * len(nums)

        cur_product = 1
        for i, num in enumerate(nums):
            result[i] = cur_product
            cur_product *= num
        print(nums)

        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result
