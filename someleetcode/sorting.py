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

if __name__ == "__main__":
    a = Sorting().quick_sort([1, 2, 7,100, 2,-1, 0.5, 3, 2, 1, 9,6,4,1])
    print(a)
