

import random


class RandomizedSet:

    def __init__(self):
        # do intialization if necessary
        self.element_list = []
        self.element_to_index = {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or 
    false
    """

    def insert(self, val):
        # write your code here
        if val in self.element_to_index:
            return False

        self.element_to_index[val] = len(self.element_list)
        self.element_list.append(val)
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """

    def remove(self, val):
        # write your code here
        if val not in self.element_to_index or not self.element_list:
            return False

        index = self.element_to_index[val]
        index_last = len(self.element_list) - 1
        last_val = self.element_list[-1]
        del self.element_to_index[val]
        self.element_list[index], self.element_list[index_last] = \
            last_val, val
        self.element_to_index[last_val] = index
        self.element_list.pop()

    """
    @return: Get a random element from the set
    """

    def getRandom(self):
        # write your code here
        return self.element_list[random.randint(0, len(self.element_list) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()