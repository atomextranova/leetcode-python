class Node:

    def __init__(self, key, val):
        self.next = None
        self.key = key
        self.val = val


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_to_prev = {}
        self.size = 0
        dummy = Node(0, 0)
        self.head = dummy
        self.tail = dummy

    #
    def pop_oldest(self):
        if self.size == 0:
            raise IndexError("No more element to be poped")

        oldest = self.head.next
        self.head.next = oldest.next
        if self.size == 1:
            self.tail = self.head

        del self.node_to_prev[oldest.key]
        self.node_to_prev[self.head.next.key] = self.head

    def append(self, key, val):
        node = Node(key, val)
        self.tail.next = node
        self.node_to_prev[node.key] = self.tail
        self.tail = node

    def make_newest(self, key):
        if self.size == 1:
            return
        parent = self.node_to_prev[key]
        cur_node = parent.next
        if cur_node == self.tail:
            return
        parent.next = cur_node.next
        self.node_to_prev[parent.next.key] = parent

        self.tail.next = cur_node
        self.node_to_prev[cur_node.key] = self.tail

        self.tail = cur_node
        cur_node.next = None

    def get(self, key: int) -> int:
        if key in self.node_to_prev:
            self.make_newest(key)
            return self.node_to_prev[key].next.val
        else:
            return -1

    # If key exists, make it the newest and change value
    # If not exists, first add it at the end(newest)
    # Then check capacity, if already max, pop the oldest
    # else size += 1
    def put(self, key: int, value: int) -> None:
        if key in self.node_to_prev:
            self.make_newest(key)
            self.node_to_prev[key].next.val = value
            return

        self.append(key, value)
        if self.size == self.capacity:
            self.pop_oldest()
        else:
            self.size += 1

# lru = LRUCache(3)
# lru.put(1, 1)
# lru.put(2, 2)
# lru.put(3, 3)
# lru.put(4, 4)
# lru.get(4)
# lru.get(3)
# lru.get(2)
# lru.get(1)
# lru.put(5, 5)
# lru.get(1)
# lru.get(2)
# lru.get(3)
# lru.get(4)
# lru.get(5)

lru = LRUCache(10)
lru.put(10, 13)
lru.put(3, 17)
lru.put(6, 11)
lru.put(10, 5)
lru.put(9, 10)
lru.get(13)
lru.put(2, 19)
lru.get(2)
lru.get(3)
# lru.get(2)
# lru.get(3)
# lru.get(4)
# lru.get(5)

# lru.put(2, 1)
# lru.get(2)
# lru.put(3, 2)
# lru.get(2)
# lru.get(3)