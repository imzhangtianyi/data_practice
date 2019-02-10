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

class BFS:
    def fun(self, m):
        visited = [False] * len(m)
        ans = 0

        for i, friends in enumerate(m):
            if visited[i]:
                continue
            ans += 1
            stack = [i]
            while stack:
                j = stack.pop()
                visited[j] = True
                for k, val in enumerate(m[j]):
                    if val and k != j and not visited[k]:
                        stack.append(k)
        return ans



if __name__ == "__main__":
    M = [[1,1,0],
        [1,1,0],
        [0,0,1]]
    d = BFS().fun(M)
    print(d)
