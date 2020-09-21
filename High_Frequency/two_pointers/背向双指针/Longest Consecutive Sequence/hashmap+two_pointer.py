class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, nums):
        # write your code here
        if not nums:
            return 0

        num_to_used = {}
        for num in nums:
            num_to_used[num] = False

        max_length = 1
        for num in num_to_used:
            if num_to_used[num] == True:
                continue

            o1 = 0
            while num + o1 in num_to_used and not num_to_used[num + o1]:
                num_to_used[num + o1] = True
                o1 += 1

            o2 = 1
            while num - o2 in num_to_used and not num_to_used[num - o2]:
                num_to_used[num - o2] = True
                o2 += 1

            max_length = max(o1 + o2 - 1, max_length)
        return max_length