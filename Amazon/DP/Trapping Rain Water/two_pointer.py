class Solution:
    # two pointer left and right going towards middle
    # record max_height from left and max_height from right
    # at each step
    # Choose the smaller size, move 1 step towards middle
    # update max_height at that side first, then calculate trapped water
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        length = len(height)
        left = 0
        right = length - 1
        left_max = height[left]
        right_max = height[right]
        result = 0
        while left < right:
            if left_max < right_max:
                left += 1
                # Update max first to avoid negative result
                left_max = max(left_max, height[left])
                result += left_max - height[left]

            else:
                right -= 1
                right_max = max(right_max, height[right])
                result += right_max - height[right]

        return result