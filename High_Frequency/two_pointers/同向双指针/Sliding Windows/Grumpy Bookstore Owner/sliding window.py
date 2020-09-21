class Solution:
    """
    @param customers: the number of customers
    @param grumpy: the owner's temper every day
    @param X: X days
    @return: calc the max satisfied customers
    """

    def maxSatisfied(self, customers, grumpy, X):
        # write your code here
        length = len(customers)

        bad_report = 0
        total_good = 0
        for i in range(X):
            if grumpy[i] == 1:
                bad_report += customers[i]
            else:
                total_good += customers[i]

        max_bad = bad_report
        for i in range(length - X):
            if grumpy[i + X] == 1:
                bad_report += customers[i + X]
            else:
                total_good += customers[i + X]

            bad_report -= customers[i] if grumpy[i] == 1 else 0
            max_bad = max(max_bad, bad_report)

        return max_bad + total_good
