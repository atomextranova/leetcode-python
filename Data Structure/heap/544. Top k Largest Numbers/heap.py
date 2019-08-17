from heapq import heappush, heappop, heappushpop


class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    # O(nlogk)
    def topk(self, nums, k):
        # write your code here
        result = [0] * k
        min_heap = []
        for i in range(k):
            heappush(min_heap, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heappushpop(min_heap, nums[i])

        for i in range(k):
            result[k - i - 1] = heappop(min_heap)

        return result