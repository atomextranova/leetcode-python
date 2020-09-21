class Solution:
    # Scan from left to right and right to left
    # to get the maximum height that height[i] could reach
    # by going left or right or itself
    # water at this block = min(left, right) - height
    # Time: O(n)
    # Space: O(n)
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        length = len(height)
        left_max = [0] * length
        right_max = [0] * length

        left_max[0] = height[0]
        for i in range(1, length):
            left_max[i] = max(height[i], left_max[i - 1])

        right_max[length - 1] = height[length - 1]
        for i in range(length - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        result = 0
        for i in range(1, length - 1):
            result += min(left_max[i], right_max[i]) - height[i]

        return result