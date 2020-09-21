class Solution:
    """
    @param arr: An integer array
    @param k: An integer
    @return: return the pair of movies index with the longest total duration
    """

    def FlightDetails(self, arr, k):
        # write your code here
        if not arr:
            return []

        k -= 30
        array = sorted(list(enumerate(arr)), key=lambda x: x[1])
        if array[0][1] + array[1][1] > k:
            return []

        left = 0
        right = len(array) - 1
        longest = -1
        result = (0, 0)
        while left < right:
            if array[left][1] + array[right][1] <= k:
                if array[left][1] + array[right][1] > longest:
                    longest = array[left][1] + array[right][1]
                    result = (array[left][0], array[right][0])
                left += 1
            else:
                right -= 1

        return sorted(result)
