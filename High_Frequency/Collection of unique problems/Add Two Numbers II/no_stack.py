class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number_1, number_2 = 0, 0
        while l1:
            number_1 = number_1 * 10 + l1.val
            l1 = l1.next
        while l2:
            number_2 = number_2 * 10 + l2.val
            l2 = l2.next
        total = number_1 + number_2
        if total == 0:
            return ListNode(0)

        head = None
        while total:
            nextDigit = total % 10
            total = total // 10
            temp = ListNode(nextDigit)
            temp.next = head
            head = temp

        return head