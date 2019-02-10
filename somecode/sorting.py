import heapq

class Sorting:
    def merge_sort(self, arr):
        """

        :param arr: list[int]
        :return: sorted List[int]
        """
        if len(arr) > 1:
            m = len(arr) // 2
            l = arr[:m]
            r = arr[m:]
            l = self.merge_sort(l)
            r = self.merge_sort(r)

            i = j = k = 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    arr[k] = l[i]
                    i += 1
                    k += 1
                else:
                    arr[k] = r[j]
                    k += 1
                    j += 1
            while i < len(l):
                arr[k] = l[i]
                k += 1
                i += 1
            while j < len(r):
                arr[k] = r[j]
                j += 1
                k += 1
        return arr

    def quick_sort(self, arr):
        """
        sort using pivot
        :param arr: list[int]
        :return: list
        """
        def pivot(arr, l, r):
            val = arr[r]
            i = l - 1
            for j in range(l, r):
                if arr[j] < val:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i+1], arr[r] = arr[r], arr[i+1]
            return arr, i+1

        if len(arr) > 1:
            arr, p = pivot(arr, 0, len(arr)-1)
            L = self.quick_sort(arr[:p])
            R = self.quick_sort(arr[p+1:])
            arr = L + [arr[p]] + R
        return arr

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        m = len(arr) // 2
        l = self.merge_sort(arr[:m])
        r = self.merge_sort(arr[m:])

        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
        return arr

    def insertion_sort(self, arr):
        """
        put smaller behind larger
        :param arr: list[int]
        :return: sorted list
        """
        for i, val in enumerate(arr[1:]):
            j = i - 1
            while j >= 0 and arr[j] > val:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = val
        return arr

    def max_heap(self, arr, i):
        n = len(arr)
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] > arr[i]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            arr = self.max_heap(arr, largest)
        return arr

    def min_heap(self, arr, i):
        n = len(arr)
        small = i
        l = i * 2 + 1
        r = i * 2 + 2

        if l < n and arr[l] < arr[i]:
            small = l
        if r < n and arr[r] < arr[small]:
            small = r
        if small != i:
            arr[small], arr[i] = arr[i], arr[small]
            arr = self.min_heap(arr, small)
        return arr

    def heap_sort(self, arr):
        for i in range(len(arr), -1, -1):
            arr = self.max_heap(arr, i)
        for i in range(len(arr)-1, 0, -1):
            arr[i], arr[0]  = arr[0], arr[i]
            self.max_heap(arr[:i], 0)
        return arr

    def heap1_sort(self, arr):
        for i in range(len(arr)-1, -1, -1):
            arr = self.max_heap(arr, i)
        temp = arr.copy()
        for i in range(len(arr)-1, -1, -1):
            arr[i] = temp[0]
            temp[i], temp[0] = temp[0], temp[i]
            temp = self.max_heap(temp[:i], 0)
        return arr

    def heap2_sort(self, arr):
        for i in range(len(arr)-1, -1, -1):
            arr = self.min_heap(arr, i)
        temp = arr.copy()
        for i in range(0, len(arr)):
            arr[i] = temp[0]
            temp = self.min_heap(temp[1:], 0)
        return arr

    def heap3_sort(self, arr):
        heapq.heapify(arr)
        h = []
        for _ in range(len(arr)):
            h.append(heapq.heappop(arr))
        return h

    def heap4_sort(self, arr):
        heapq._heapify_max(arr)
        h = []
        for _ in range(len(arr)):
            h.append(heapq._heappop_max(arr))
        return h[::-1]



if __name__ == "__main__":
    a = Sorting().m_sort([1, 2, 7,10, 2,-1, 0.5, -3, 2, 1, 9,6,4,1, 32, 14, 0])
    print(a)
