# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from heapq import heappush, heappop

ListNode.__lt__ = lambda x, y: (x.val < y.val)
class Solution:
    # Use heap
    # O(nlogk)
    # Overwrite __It__ of ListNode
    # Edge cases:
    # []
    # [None, None]
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        min_heap = []

        for node in lists:
            # Avoid adding None
            if not node:
                continue
            heappush(min_heap, (node.val, node))

        dummy = ListNode(-1)
        root = dummy
        while len(min_heap) > 0:
            val, node = heappop(min_heap)
            root.next = node
            root = node
            node = node.next
            if (node):
                heappush(min_heap, (node.val, node))

        return dummy.next