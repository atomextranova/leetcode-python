class Solution:
    # if  nums[mid] > nums[mid+1], search left
    # <: search right
    # ==: search either direction
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return 0

        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid
            else:
                right = mid
        if nums[left] > nums[right]:
            return left
        else:
            return right