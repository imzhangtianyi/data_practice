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


if __name__ == "__main__":
    a = Sorting().merge_sort([1, 2, 3, 2, 1])
    print(a)
