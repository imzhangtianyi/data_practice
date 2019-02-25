class Solution:
    def gen(self, n):
        ans = []

        def helper(arr, N):
            if len(arr) == N:
                s = ''.join(arr)
                if self.valid(s):
                    ans.append(s)
            elif len(arr) < N:
                # arr.append('(')
                arr = arr + ['(']
                helper(arr, N)
                arr.pop()
                # arr.append(')')
                arr = arr + [')']
                helper(arr, N)
                # arr.pop()
        helper([], 2*n)
        return ans




    def valid(self, s):
        num = 0
        for ch in s:
            if ch == '(':
                num += 1
            else:
                num -= 1
            if num < 0:
                return False
        return not num

    def backtrack(self, n):
        N = n * 2
        ans = []

        def helper(s, l, r):
            if len(s) == N:
                ans.append(s)
                return
            if l < n:
                helper(s+'(', l+1, r)
            if r < l:
                helper(s+')', l, r+1)
        helper('', 0, 0)
        return ans


print(Solution().gen(3))