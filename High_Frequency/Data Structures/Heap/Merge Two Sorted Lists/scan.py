# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2

        if not l2:
            return l1

        dummy = ListNode(-1)
        temp = dummy
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
                temp = temp.next
            else:
                temp.next = l2
                l2 = l2.next
                temp = temp.next

        while l1:
            temp.next = l1
            l1 = l1.next
            temp = temp.next

        while l2:
            temp.next = l2
            l2 = l2.next
            temp = temp.next

        return dummy.next

