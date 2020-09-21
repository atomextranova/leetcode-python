class Solution:
    """
    @param boxes: number of pens for each box
    @param target: the target number
    @return: the minimum boxes
    """
    # 1. prefix sum + hashmap to find the minimum valid array length
    # at each index for the array
    # 2. The same array for right
    # 3. For index, find length sum for left[0, i] + right[i+1, length-1]
    def minimumBoxes(self, boxes, target):
        # write your code here
        left = self.find_valid_array(boxes, target)
        right = self.find_valid_array(boxes[::-1], target)
        right = right[::-1]

        min_length = float('inf')
        for i in range(len(boxes) - 1):
            min_length = min(min_length, left[i] + right[i+1])

        return min_length if min_length != float('inf') else -1

    def find_valid_array(self, boxes, target):
        sum_to_index = {}
        cur_sum = 0
        min_lengths = [float('inf')] * len(boxes)
        sum_to_index[0] = -1

        for i, val in enumerate(boxes):
            cur_sum += val
            diff = cur_sum - target

            if diff in sum_to_index:
                min_lengths[i] = min(min_lengths[i-1], i - sum_to_index[diff])
            else:
                min_lengths[i] = min_lengths[i-1]

            sum_to_index[cur_sum] = i

        return min_lengths