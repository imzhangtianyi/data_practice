class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False

        if self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        elif self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1
        return True


class DSU2:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        self.parent[xr] = yr
        return True

class Solution:
    def findRedundantConnection(self, edges):
        graph = {}
        self.seen = set()

        for x, y in edges:
            if x in graph and y in graph and self.dfs(x, y, graph):
                return x, y
            if x not in graph:
                graph[x] = [y]
            elif x in graph:
                graph[x].append(y)
            if y not in graph:
                graph[y] = [x]
            elif y in graph:
                graph[y].append(x)

    def dfs(self, x, y, graph):
        if x not in self.seen:
            self.seen.add(x)
            if x == y:
                return True
            return any(self.dfs(neighbor, y, graph) for neighbor in graph[x])

    def union_find(self, edges):
        dsu = DSU2(100)
        for x, y in edges:
            if not dsu.union(x, y):
                return x, y


if __name__ == "__main__":
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    ans = Solution().union_find(edges)
    print(ans)
