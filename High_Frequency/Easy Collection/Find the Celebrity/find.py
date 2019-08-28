"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""


class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        target = 0
        for i in range(n):
            if Celebrity.knows(target, i):
                target = i
        for i in range(n):
            if Celebrity.knows(target, i) and target != i:
                return -1
            if not Celebrity.knows(i, target):
                return -1

        return target