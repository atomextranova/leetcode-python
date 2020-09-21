from collections import defaultdict, deque


class Solution:

    # Traverse point (i, j) in the same sequence if i + j is equal
    # Note different orders for different result of (i + j % 2)
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        cur_dict = defaultdict(deque)
        max_key = len(matrix) + len(matrix[0]) - 2
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dict_key = i + j
                if dict_key % 2 == 0:
                    cur_dict[dict_key].appendleft(matrix[i][j])
                else:
                    cur_dict[dict_key].append(matrix[i][j])

        result = []
        for i in range(max_key + 1):
            for element in cur_dict[i]:
                result.append(element)

        return result