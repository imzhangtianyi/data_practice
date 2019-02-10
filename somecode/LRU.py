class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: 'int'):
        self.cap = capacity
        self.dict = dict()
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: 'int') -> 'int':
        if key in self.dict:
            node = self.dict[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head.next
            node.prev = self.head
            node.next.prev = node
            self.head.next = node
            return node.val
        else:
            return -1

    def put(self, key: 'int', val: 'int'):
        if key in self.dict:
            node = self.dict[key]
            node.val = val
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head.next
            node.prev = self.head
            node.next.prev = node
            self.head.next = node
        else:
            if len(self.dict) == self.cap:
                delete_node = self.tail.prev
                del self.dict[delete_node.key]
                delete_node.prev.next = self.tail
                self.tail.prev = delete_node.prev
                delete_node.next = None
                delete_node.next = None
            new_node = ListNode(key, val)
            self.dict[key] = new_node
            new_node.next = self.head.next
            new_node.next.prev = new_node
            self.head.next = new_node
            new_node.prev = self.head


if __name__ == "__main__":
    cache = LRUcache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1)) # returns 1
    cache.put(3, 3) # evicts key 2
    print(cache.get(2)) # returns - 1(not found)
    cache.put(4, 4) # evicts key 1
    print(cache.get(1)) # returns - 1(not found)
    print(cache.get(3)) # returns 3
    print(cache.get(4)) # returns 4


