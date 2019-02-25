class Solution:

    def fun(self, arr):
        res = []
        for p in sorted(arr, key=lambda x: (-x[0], x[1])):
            res.insert(p[1], p)
        return res

    def quick_sort(self, arr, l, r, key):
        if l < r:
            pivot = self.partition(arr, l, r, key)
            self.quick_sort(arr, l, pivot-1, key)
            self.quick_sort(arr, pivot+1, r, key)
        return arr

    def partition(self, arr, l, r, key):
        pivot = arr[r][key]
        larger = l - 1
        for i in range(l, r):
            if arr[i][key] <= pivot:
                larger += 1
                arr[larger], arr[i] = arr[i], arr[larger]
        arr[larger+1], arr[r] = arr[r], arr[larger+1]
        return larger+1

    def fun2(self, arr):
        n = len(arr)
        arr = self.quick_sort(arr, 0, n-1, 0)[::-1]
        l = 0
        r = 0
        while l < n and r < n:
            if arr[r][0] == arr[l][0]:
                r += 1
            else:
                arr = self.quick_sort(arr, l, r-1, 1)
                l = r

        res = []
        for p in arr:
            if len(res) <= p[1]:
                res.append(p)
            else:
                i = p[1]
                while i < len(res):
                    temp = res[i]
                    res[i] = p
                    p = temp
                    i += 1
                res.append(p)
        return res


if __name__ == "__main__":
    arr = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2], [6,0]]
    print(sorted(arr, key=lambda x: (-x[0], x[1])))
    print(Solution().fun(arr))
    print(Solution().fun2(arr))