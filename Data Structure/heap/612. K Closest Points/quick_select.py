class Solution:
    def kClosest(self, points, K: int) -> List[List[int]]:
        distance_list = [self.calculate_distance(point) for point in points]
        length = len(points)
        if length == K:
            return points
        self.quick_select(points, distance_list, 0, length - 1, K)
        return points[:K]

    def quick_select(self, nums, distance_list, start, end, k):
        if start == end:
            return

        left, right = start, end
        pivot = distance_list[(left + right) // 2]
        while left <= right:
            while left <= right and distance_list[left] < pivot:
                left += 1
            # Only >, not =
            while left <= right and distance_list[right] > pivot:
                right -= 1
            if left <= right:
                distance_list[left], distance_list[right] = distance_list[
                                                                right], \
                                                            distance_list[left]
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if k <= right:
            self.quick_select(nums, distance_list, start, right, k)
        if k >= left:
            self.quick_select(nums, distance_list, left, end, k)

    def calculate_distance(self, point):
        return point[0] ** 2 + point[1] ** 2
