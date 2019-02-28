class Solution:
    def fun1(self, n: int, k: int):
        if n == 0 and k == 0:
            return [[]]
        if n < k:
            return []
        ans = self.dfs(n, k, [], [])
        return ans

    def dfs(self, n, k, path, res):
        if not k:
            res.append(path)
            return
        for i in range(1, n + 1):
            self.dfs(i - 1, k - 1, path + [i], res)
        return res

    def fun2(self, n, k):
        temp = []
        for i in range(k, n+1):
            temp.append([i])

        for _ in range(k-1):
            comb = temp
            temp = []
            for arr in comb:
                for i in range(1, arr[-1]):
                    temp.append(arr + [i])
        return temp

    def fun3(self, n, k):
        ans = [[]]
        for _ in range(k):
            ans = [[i] + comb for comb in ans for i in range(1, comb[0] if comb else n+1)]
        return ans


if __name__ == "__main__":
    print(Solution().fun3(5,3))