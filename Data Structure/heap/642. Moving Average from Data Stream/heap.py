# Given a stream of integers and a window size, calculate the moving average
# of all integers in the sliding window.
#
# Example
# Example 1:
#
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1 // return 1.00000
# m.next(10) = (1 + 10) / 2 // return 5.50000
# m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
# m.next(5) = (10 + 3 + 5) / 3 // return 6.00000

from collections import deque


class MovingAverage:
    """
    @param: size: An integer
    """

    def __init__(self, size):
        # do intialization if necessary
        self.stack = deque([])
        self.cur_sum = 0
        self.size = size

    """
    @param: val: An integer
    @return:  
    """

    def next(self, val):
        # write your code here
        if len(self.stack) == self.size:
            self.cur_sum -= self.stack.popleft()
        self.cur_sum += val
        self.stack.append(val)
        return self.cur_sum / len(self.stack)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)
