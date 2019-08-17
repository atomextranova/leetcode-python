class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        # write your code here
        if k <= 0 or not colors:
            return colors
        self.sort_color(colors, 1, k, 0, len(colors) - 1)

    def sort_color(self, colors, color_low, color_high, start, end):
        if color_low == color_high or start == end:
            return

        pivot = (color_low + color_high) // 2
        left, right = start, end
        while left <= right:
            # must be <= so that it works when pivot is lowest value of the array
            # e.g. [2, 1. 2], k = 2
            while left <= right and colors[left] <= pivot:
                left += 1
            while left <= right and colors[right] > pivot:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
        self.sort_color(colors, color_low, pivot, start, right)
        self.sort_color(colors, pivot + 1, color_high, left, end)