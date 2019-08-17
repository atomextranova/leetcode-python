

from collections import deque


class Stack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def swap(self):
        self.queue1, self.queue2 = self.queue2, self.queue1

    def move_item(self):
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

    """
    @param: x: An integer
    @return: nothing
    """

    def push(self, x):
        # write your code here
        self.queue1.append(x)

    """
    @return: nothing
    """

    def pop(self):
        # write your code here
        self.move_item()
        self.queue1.popleft()
        self.swap()

    """
    @return: An integer
    """

    def top(self):
        # write your code here
        self.move_item()
        item = self.queue1[0]
        self.queue2.append(self.queue1.popleft())
        self.swap()
        return item

    """
    @return: True if the stack is empty
    """

    def isEmpty(self):
        # write your code here
        return len(self.queue1) == 0
