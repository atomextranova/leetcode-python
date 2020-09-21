# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# first get tow numbers
# then get the result
# use a stack to store numbers
# then create new pointers
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number_1 = 0
        while l1:
            number_1 = number_1 * 10 + l1.val
            l1 = l1.next

        number_2 = 0
        while l2:
            number_2 = number_2 * 10 + l2.val

        num = num = number_1 + number_2

        stack = []
        while num != 0:
            stack.append(num % 10)
            num = num // 10

        dummy = ListNode(-1)
        temp = dummy
        while stack:
            val = stack.pop()
            temp.next = ListNode(val)
            temp = temp.next

        return dummy.next
    
sol = Solution()
print(sol.addTwoNumbers())