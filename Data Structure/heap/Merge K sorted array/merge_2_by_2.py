class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        while len(arrays) > 1:
            next_arrays = []
            for i in range(0, len(arrays), 2):
                if i + 1 < len(arrays):
                    array = self.merge_two_arrays(arrays[i], arrays[i + 1])
                else:
                    array = arrays[i]
                next_arrays.append(array)
            arrays = next_arrays

        return arrays[0]

    def merge_two_arrays(self, arr1, arr2):
        i, j = 0, 0
        array = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                array.append(arr1[i])
                i += 1
            else:
                array.append(arr2[j])
                j += 1
        while i < len(arr1):
            array.append(arr1[i])
            i += 1
        while j < len(arr2):
            array.append(arr2[j])
            j += 1
        return array