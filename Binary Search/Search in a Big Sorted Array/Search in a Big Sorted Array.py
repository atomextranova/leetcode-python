"""
Definition of ArrayReader
class ArrayReader(object):
    def get(self, index):
    	# return the number on given index,
        # return 2147483647 if the index is invalid.
"""
class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # Store temporary value
        first_index = 0
        first_val = reader.get(first_index)
        if target < first_val:
            return -1
        last_index = 1
        last_val = reader.get(last_index)
        while last_val < target:
            last_index = last_index << 1
            last_val = reader.get(last_index)
            # Using this as right bound if out of bound
            if last_val >= 2147483647:
                break
        # Shift operation
        first_index = last_index >> 1
        first_val = reader.get(first_index)

        while first_index + 1 < last_index:
            mid = first_index + ((last_index - first_index) >> 1)
            mid_val = reader.get(mid)
            if mid_val < target:
                first_index = mid
                first_val = mid_val
            if mid_val > target:
                last_index = mid
                last_val = mid_val
            if mid_val == target:
                # Keep searching even if found target since we want first target
                last_index = mid
                last_val = mid_val

        if first_val == target:
            return first_index
        if last_val == target:
            return last_index
        return -1

class ArrayReader:

    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def get(self, index):
        if index < self.length:
            return self.array[index]
        else:
            return 2147483647

sol = Solution()
print(sol.searchBigSortedArray(ArrayReader([1,2,3,4,5,6]), 6))