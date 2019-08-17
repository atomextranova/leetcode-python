class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """

    def triangleCount(self, S):
        # write your code here
        if not S:
            return 0
        S.sort()
        count = 0
        for third in range(len(S)):
            left = 0
            right = third - 1
            while left < right:
                if S[left] + S[right] <= S[third]:
                    left += 1
                elif S[left] + S[right] > S[third]:
                    count += right - left
                    right -= 1

        return count