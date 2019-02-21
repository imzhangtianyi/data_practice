import heapq


class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, num: 'int') -> 'None':
        heapq.heappush(self.heap, num)

    def pop(self) -> 'int':
        return heapq.heappop(self.heap)

    def peek(self) -> 'int':
        return self.heap[0]

    def __len__(self) -> 'int':
        return len(self.heap)


class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, num: 'int') -> 'None':
        heapq.heappush(self.heap, num * -1)

    def pop(self) -> 'int':
        return heapq.heappop(self.heap) * -1

    def peek(self) -> 'int':
        return self.heap[0] * -1

    def __len__(self) -> 'int':
        return len(self.heap)


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = MaxHeap()
        self.right = MinHeap()
        self.median = 0.0

    def addNum(self, num: 'int') -> 'None':
        if self.left.__len__() == self.right.__len__():
            if num >= self.median:
                self.right.push(num)
                self.median = self.right.peek()
            else:
                self.left.push(num)
                self.median = self.left.peek()
        elif self.left.__len__() < self.right.__len__():
            if num >= self.median:
                temp = self.right.pop()
                self.left.push(temp)
                self.right.push(num)
            else:
                self.left.push(num)
            self.median = (self.left.peek() + self.right.peek()) / 2
        else:
            if num >= self.median:
                self.right.push(num)
            else:
                temp = self.left.pop()
                self.right.push(temp)
                self.left.push(num)
            self.median = (self.left.peek() + self.right.peek()) / 2

    def findMedian(self) -> 'float':
        return self.median