# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        m = len(isConnected[0])

        graph = defaultdict(list)
        for r in range(n):
            for c in range(m):
                if r != c and isConnected[r][c]:
                    graph[r].append(c)
                    graph[c].append(r)

        def dfs(node, visited):
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh, visited)
        
        count = 0
        visited = set()
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node, visited)
        return count

