# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for row, col in edges:
            graph[row].append(col)
            graph[col].append(row)
        visited = set()
        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    found = dfs(neigh, visited)
                    if found:
                        return True
            return False
        return dfs(source, visited)