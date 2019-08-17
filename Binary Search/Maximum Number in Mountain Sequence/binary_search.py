class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """

    def mountainSequence(self, nums):
        # write your code here
        if not nums:
            return -1
        start_index = 0
        end_index = len(nums) - 1
        mid_index = 0
        while start_index + 1 < end_index:
            # Or use // 2 to make sure mid_index + Triangle Count in bound
            mid_index = start_index + ((end_index - start_index) >> 1)
            if nums[mid_index] < nums[mid_index + 1]:
                start_index = mid_index
            else:
                end_index = mid_index

        return max(nums[start_index], nums[end_index])