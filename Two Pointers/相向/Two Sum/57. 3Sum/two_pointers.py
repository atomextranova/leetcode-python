class Solution:
    def threeSum(self, nums):
        if not nums:
            return []

        nums.sort()
        length = len(nums)
        result = []
        last_val = None
        for i, num in enumerate(nums):
            if last_val == num:
                continue
            last_val = num
            target_sum = -num
            cur_result = self.two_sum(nums, target_sum, i + 1, length - 1)
            result.extend(cur_result)
        return result

    def two_sum(self, nums, target_sum, start, end):
        temp_result = []
        while start < end:
            cur_sum = nums[start] + nums[end]
            if cur_sum < target_sum:
                start += 1
            elif cur_sum > target_sum:
                end -= 1
            else:
                temp_result.append((-target_sum, nums[start], nums[end]))
                # Avoid duplicates in current result
                while start < end and nums[start + 1] == nums[start]:
                    start += 1
                while start < end and nums[end - 1] == nums[end]:
                    end -= 1

                # Key, start next after duplicates have been removed
                # If update start and end first, will lose result
                # E.g. [-2,0,1,1,2]
                start += 1
                end -= 1

        return temp_result



sol = Solution()
print(sorted(sol.threeSum([-2,0,1,1,2])))