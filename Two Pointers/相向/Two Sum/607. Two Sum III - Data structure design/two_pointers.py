class TwoSum:
    def __init__(self):
        self.table = {}

    """
    @param number: An integer
    @return: nothing
    """

    def add(self, number):
        # write your code here
        if number in self.table:
            self.table[number] += 1
        else:
            self.table[number] = 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        for key in self.table.keys():
            diff = value - key
            if diff == key:
                if self.table[key] >= 2:
                    return True
            else:
                if diff in self.table:
                    return True

        return False