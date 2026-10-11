class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
        self.cache = {} # key: int, val: node

    def get(self, key: int) -> int:
        if key not in self.cache: return -1

        node = self.cache[key]

        if self.head == self.tail or self.tail == node: 
            return node.val

        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
            node.next = None

        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
            node.next = None

        return node.val
            

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            node = self.cache[key]

            if self.tail == node: 
                return

            elif self.head == node:
                self.head = self.head.next
                self.head.prev = None
                self.tail.next = node
                node.prev = self.tail
                self.tail = self.tail.next
                node.next = None

            else:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.tail.next = node
                node.prev = self.tail
                self.tail = self.tail.next
                node.next = None

            return

        if self.size == self.capacity:
            del self.cache[self.head.key] 
            self.size -= 1
            self.head = self.head.next
            if not self.head: self.tail = None
            else: self.head.prev = None

        node = ListNode(key, value)
        self.cache[key] = node
        self.size += 1

        if not self.head and not self.tail:
            self.head, self.tail = node, node

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None