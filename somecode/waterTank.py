def two_pointers(arr):
    ans = 0
    l = 0
    r = len(arr) - 1
    min_height = 0

    while l < r:
        while l < r and arr[l] <= min_height:
            ans += min_height - arr[l]
            l += 1
        while l < r and arr[r] <= min_height:
            ans += min_height - arr[r]
            r -= 1
        min_height = min(arr[l], arr[r])
    return ans

def dp(arr):
    def trap(self, arr: 'List[int]') -> 'int':
        max_l = []
        m = float('-inf')
        for i in arr:
            m = max(m, i)
            max_l.append(m)

        max_r = []
        m = float('-inf')
        for i in reversed(arr):
            m = max(m, i)
            max_r.append(m)
        max_r.reverse()

        ans = 0

        for h, l, r in zip(arr, max_l, max_r):
            ans += min(l, r) - h
        return ans

if __name__ == "__main__":
    arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(two_pointers(arr))