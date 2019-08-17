class DoublyLinkedListNode:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.val_to_node = {}

    def append(self, val):
        node = DoublyLinkedListNode(val)
        self.
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def insert_after(self, node, val):
        new_node = DoublyLinkedListNode(val)
        if node.next is None:
            node.next = new_node
            new_node.prev = node
            self.tail = new_node
        else:
            next_node = node.next
            node.next = new_node
            next_node.prev = new_node
            new_node.next = next_node
            new_node.prev = node

    def remove(self, node):
        if node.prev is None:
            self.head = self.tail