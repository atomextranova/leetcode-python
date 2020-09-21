"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    # Create map: old_node -> new_node
    # Traverse the old list, for each node
    # create(if not present in the dict) or
    # get the corresponding new node by checking mapping
    # of old node
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        old_node = head
        new_node = Node(head.val, None, None)
        self.visited = {}
        self.visited[old_node] = new_node

        while old_node != None:
            new_node.next = self.get_node(old_node.next)
            new_node.random = self.get_node(old_node.random)
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]

    def get_node(self, old_node):
        if not old_node:
            return None

        if old_node not in self.visited:
            self.visited[old_node] = Node(old_node.val, None, None)

        return self.visited[old_node]