from collections import defaultdict


class DFS:
    def fun(self, equations, values, queries):
        graph = defaultdict(dict)
        for (x, y), value in zip(equations, values):
            graph[x][y] = value
            graph[y][x] = 1 / value
            graph[x][x] = graph[y][y] = 1

        ans = []
        for x, y in queries:
            ans.append(self.dfs(x, y, graph, set()))
        return ans

    def dfs(self, start, end, graph, visited):
        if start not in graph:
            return -1
        if end in graph[start]:
            return graph[start][end]
        for key, val in graph[start].items():
            if key not in visited:
                visited.add(key)
                new_val = self.dfs(key, end, graph, visited)
                if val != -1:
                    return val * new_val
                visited.discard(key)
        return -1


if __name__ == "__main__":
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(DFS().fun(equations, values, queries))
