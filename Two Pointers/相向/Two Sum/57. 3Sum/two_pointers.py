class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # write your code here

        numbers.sort()
        print(numbers)
        result = []
        third = len(numbers) - 1
        last_val = None
        while third > 1:
            third_val = numbers[third]
            if third_val == last_val:
                third -= 1
                continue
            target = -third_val
            self.two_sum_helper(numbers, target, third, result)
            third -= 1
            last_val = third_val
        return result

    def two_sum_helper(self, nums, target, third, result):
        # write your code here

        left = 0
        right = third - 1

        while left < right:
            left_val = nums[left]
            right_val = nums[right]

            if left_val + right_val < target:
                left += 1
            elif left_val + right_val > target:
                right -= 1
            else:
                result.append([left_val, right_val, nums[third]])
                left += 1
                right -= 1

                while nums[left] == left_val and left < right:
                    left += 1
                while nums[right] == right_val and left < right:
                    right -= 1


sol = Solution()
print(sorted(sol.threeSum([-2,-3,-4,-5,-100,99,1,4,4,4,5,1,0,-1,2,3,4,5])))