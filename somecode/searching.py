class C:
    def linear_search(self, arr, k):
        """
        linear time
        :param arr: list[int]
        :param k: int
        :return: index
        """
        for i, num in enumerate(arr):
            if num == k:
                return i

    def binary_search(self, arr, k):
        """
        log n time
        :param arr: list[int]
        :param k: int
        :return: index
        """
        l = 0
        r = len(arr) - 1

        while l <= r:
            m = (l + r) // 2
            if arr[m] == k:
                return m
            elif arr[m] < k:
                l = m + 1
            else:
                r = m - 1


if __name__ == "__main__":
    arr = list(range(10**5))
    print(C().binary_search(arr,3**5))

