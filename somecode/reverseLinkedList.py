class ListNode:
    def __init__(self, x):
        """
        this is a doubly linked list node
        :param x: data
        """
        self.val = x
        self.prev = None
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = ListNode(data)
        node.next = self.head

        if self.head:
            self.head.prev = node

        self.head = node

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            prev = curr.prev
            curr.prev = curr.next
            curr.next = prev
            curr = curr.prev

        if prev:
            self.head = prev.prev


if __name__ == "__main__":
    arr = list(range(5))
    head = List()
    for i in arr:
        head.push(i)

    node = head.head
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    print(arr)

    head.reverse()

    node = head.head
    arr = []
    print(node)
    while node:
        arr.append(node.val)
        node = node.next
    print(arr)
