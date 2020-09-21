from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        left = 0
        right = len(nums) - 1

        # max_possible_missing = len(nums) + 1
        # Left store small numbers, num[i] = i + 1
        # left will end up being the index for first missing positive
        # so first missing = left + 1
        # right half store numbers that do not need to consider to be put at left

        # Stop Until left/right pass each other
        # e.g. [1], end up with left = 1, right = 0
        while left <= right:
            cur_val = nums[left]

            # if cur_val successfully placed, update left to find next match
            if cur_val == left + 1:
                left += 1

            # Not a candiate for missing in 3 cases, put them at the right half
            # 1. > right index + 1, too large
            # so first missing must happen before it
            # 2. <= 0, too small that first missing must be after it
            # 3. duplicate values found, cur_val has a duplicate value placed
            # at the right place num[cur_val] - 1, so we put cur_val here at
            # right and check the new swapped value again
            elif cur_val > right + 1 or cur_val <= 0 or nums[
                cur_val - 1] == cur_val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            # put current value at the right place, but this place may be left
            # part or right part. Will decide later in later loop when
            # we update left/right.
            else:
                nums[left], nums[cur_val - 1] = nums[cur_val - 1], nums[left]

        return left + 1


sol = Solution()
print(sol.firstMissingPositive([3, 4, 3, 1]))
