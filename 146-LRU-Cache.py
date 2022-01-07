class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        # double linked list
        self.cap = capacity
        self.cache = {}
        self.head = Node(None,None)
        self.tail = Node(None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        node.prev, node.next = None, None
        
    def insert(self, node):
        # insert to the very front
        n = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = n
        n.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            if len(self.cache) == self.cap:
                node = self.tail.prev
                p = node.prev
                p.next = self.tail
                self.tail.prev = p
                self.cache.pop(node.key)
            node = Node(key, value)
            n = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = n
            n.prev = node
            self.cache[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
