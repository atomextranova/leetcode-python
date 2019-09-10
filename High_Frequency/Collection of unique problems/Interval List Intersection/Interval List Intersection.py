class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> \
    List[List[int]]:
        left = 0
        right = 0
        result = []
        while left < len(A) and right < len(B):
            cur_start = max(A[left][0], B[right][0])
            cur_end = min(A[left][1], B[right][1])
            if cur_start <= cur_end:
                result.append((cur_start, cur_end))
            # Add the index of list which has smaller end
            if A[left][1] > B[right][1]:
                right += 1
            else:
                left += 1

        return result