import heapq


class MinHeap:
    def __init__(self):
        """
        a min heap will be on the right side
        """
        self.heap = []

    def push(self, num):
        heapq.heappush(self.heap, num)

    def pop(self):
        return heapq.heappop(self.heap)

    def peek(self):
        return self.heap[0]

    def __len__(self):
        return len(self.heap)


class MaxHeap:
    def __init__(self):
        """
        a min heap will be on the right side
        """
        self.heap = []

    def push(self, num):
        heapq.heappush(self.heap, num*-1)

    def pop(self):
        return heapq.heappop(self.heap*-1)

    def peek(self):
        return self.heap[0]*-1

    def __len__(self):
        return len(self.heap)


class MedianFinder:
    def __init__(self):
        """
        initialize heaps
        """
        self.right = MinHeap()
        self.left = MaxHeap()
        self.median = 0.0

    def addNum(self, num):
        if self.left.__len__() == self.right.__len__():
            if num < self.median:
                self.left.push(num)
                self.median = self.left.peek()
            else:
                self.right.push(num)
                self.median = self.right.peek()

        elif self.left.__len__() > self.right.__len__():
            if num < self.median:
                self.right.push(self.left.pop())
                self.left.push(num)
            else:
                self.right.push(num)
            self.median = (self.left.peek() + self.right.peek()) / 2

        else:
            if num < self.median:
                self.left.push(num)
            else:
                self.left.push(self.right.pop())
                self.right.push(num)
            self.median = (self.left.peek() + self.right.peek()) / 2

    def findMedian(self):
        """
        get the median number
        :return: float
        """
        return self.median
