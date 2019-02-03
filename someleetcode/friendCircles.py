class DFS:
    def fun(self, m):
        ans = 0
        visited = [False] * len(m)
        for i in range(len(m)):
            if not visited[i]:
                ans += 1
                self.dfs(m, visited, i)
        return ans

    def dfs(self, m, visited, i):

        neighbors = m[i]

        for j, know in enumerate(neighbors):
            if know and not visited[j]:
                visited[j] = True
                self.dfs(m, visited, j)


if __name__ == "__main__":
    M = [[1,1,0],
        [1,1,0],
        [0,0,1]]
    d = BFS().fun(M)
    print(d)
