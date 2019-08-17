class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """

    # Edge case:
    # nums = []
    # k > len(nums) / k < 0
    # How duplicates are arranged

    # QuickSelect
    # O(n)
    def kthSmallest(self, k, nums):
        # write your code here

        if not nums or k < 1 or k > len(nums):
            return None

        return self.quick_select(k - 1, nums, 0, len(nums) - 1)

    def quick_select(self, k, nums, start, end):
        if start == end:
            return nums[start]

        # Partition array according to pivot
        left, right = start, end
        pivot_val = nums[(end - start) // 2 + start]
        while left <= right:
            while left <= right and nums[left] < pivot_val:
                left += 1
            while left <= right and nums[right] > pivot_val:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if k <= right:
            self.quick_select(k, nums, start, right)

        if k >= left:
            self.quick_select(k, nums, left, end)

        return nums[k]

