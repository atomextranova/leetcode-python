class Solution:
    """
    @param boxes: number of pens for each box
    @param target: the target number
    @return: the minimum boxes
    """
    # 1. Two pointer to form an array that records for each index i, the length
    # of the shortest valid array sum == target in range(0, i+1)
    # 2. The same array for right
    # 3. For index, find length sum for left[0, i] + right[i+1, length-1]

    # Time: O(n)
    # O(n) for valid array from left, O(n) for the array from right,
    # O(n) for enumerating the dividing index to find the minimum sum
    # Space: O(n)
    def minimumBoxes(self, boxes, target):
        # write your code here
        left = self.get_minimum_length_valid_array(boxes, target)

        # Reverse to reuse
        boxes = boxes[::-1]
        right = self.get_minimum_length_valid_array(boxes, target)
        right = right[::-1]

        # Len - 1 to resolve index error
        min_length = float('inf')
        for i in range(len(boxes) - 1):
            min_length = min(left[i] + right[i + 1], min_length)

        if min_length == float('inf'):
            return -1

        return min_length


    def get_minimum_length_valid_array(self, boxes, target):
        valid_length_array = [float('inf')] * len(boxes)
        left = 0
        right = 0
        cur_sum = 0

        while right < len(boxes):
            cur_sum += boxes[right]
            # Find a range < target
            while cur_sum > target:
                cur_sum -= boxes[left]
                left += 1

            if cur_sum == target:
                cur_length = right - left + 1
                valid_length_array[right] = min(valid_length_array[right - 1],
                                                cur_length)
            else:
                valid_length_array[right] = valid_length_array[right - 1]

            right += 1

        return valid_length_array
