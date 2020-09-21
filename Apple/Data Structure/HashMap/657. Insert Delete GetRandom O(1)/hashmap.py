import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_to_index = dict()
        self.element_list = []
    # Add to list
    # record element index
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already
        contain the specified element.
        """
        if val in self.val_to_index:
            return False

        self.val_to_index[val] = len(self.element_list)
        self.element_list.append(val)
        return True

    # Swap last element with to element to be removed
    # set last element's new index
    # Remove current last element from dict and list
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the
        specified element.
        """
        if val not in self.val_to_index:
            return False

        remove_index = self.val_to_index[val]
        self.val_to_index[self.element_list[-1]] = remove_index
        self.element_list[-1], self.element_list[remove_index] = \
        self.element_list[remove_index], self.element_list[-1]
        self.element_list.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.element_list[random.randint(0, len(self.element_list) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()