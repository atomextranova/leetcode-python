class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        target = nums[right]

        # Pivot value = end of array
        # end is max value if array is not sorted,
        # so always seach left in that case
        # Otherwise, pivot < nums[0] initially
        # nums[mid] > pivot -> we need to search right
        # to find the sorted part that contains
        # smaller values of the original array
        # nums[mid] =< pivot
        # Now we are at the array where (left, mid)
        # contains the minimum value
        while left + 1 < right:
            mid = (left + right) // 2
            print(nums[mid])
            if nums[mid] > target:
                left = mid
            elif nums[mid] < target:
                right = mid
            else:
                right = mid

        return min(nums[left], nums[right])