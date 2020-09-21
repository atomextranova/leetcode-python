class DoublyLinkedListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.key_to_prev_node = {}
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.key_to_node = {}
        self.size = 0

    def append(self, key, val):
        node = DoublyLinkedListNode(key, val)
        self.key_to_node[key] = node
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def pop(self):
        node = self.head
        next_node = node.next
        if next_node is None:
            self.head = None
            self.tail = None
        else:
            self.head = next_node
            next_node.prev = None
            self.next = next_node
        del self.key_to_node[node.key]

    def refresh(self, key, val):
        # Always change value first even not changing position
        node = self.key_to_node[key]
        node.val = val
        if self.head == self.tail:
            return
        prev_node = node.prev
        next_node = node.next
        if next_node == None:
            return
        if prev_node == None:
            self.head = next_node
            next_node.prev = None
        else:
            next_node.prev = prev_node
            prev_node.next = next_node

        node.prev = self.tail
        node.next = None
        self.tail.next = node
        self.tail = node



    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self.refresh(key, node.val)
        self.show("get", key, node.val)
        return node.val

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def put(self, key, value):
        # write your code here
        if key not in self.key_to_node:
            if self.size == self.capacity:
                self.pop()
                self.size -= 1
            self.append(key, value)
            self.size += 1
        else:
            self.refresh(key, value)
        self.show("set", key, value)


    def show(self, method, key, value):
        node = self.head
        str_list = []
        while node != None:
            str_list.append("%s:%s" % (node.val, node.key))
            node = node.next
        print("%s (%d, %d): %s" %(method, key, value, '->'.join(str_list)))

lru = LRUCache(3)
lru.put(1, 1)
lru.put(2, 2)
lru.put(3, 3)
lru.put(4, 4)
lru.get(4)
lru.get(3)
lru.get(2)
lru.get(1)
lru.put(5, 5)
lru.get(1)
lru.get(2)
lru.get(3)
lru.get(4)
lru.get(5)