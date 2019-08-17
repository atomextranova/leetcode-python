class MinStack:
    # Edge case:
    # first push
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.min_stack = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        # write your code here
        self.stack.append(number)

        # first push
        if not self.min_stack:
            self.min_stack.append(number)
            return
        last_min = self.min_stack[-1]
        if number > last_min:
            self.min_stack.append(last_min)
        else:
            self.min_stack.append(number)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here

        self.min_stack.pop()

        return self.stack.pop()

    """
    @return: An integer
    """

    def min(self):
        # write your code here
        return self.min_stack[-1]
