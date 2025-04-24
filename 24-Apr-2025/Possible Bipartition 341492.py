# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        color = [-1] * (n + 1)

        def dfs(node):
            for neigh in graph[node]:
                if color[neigh] == -1:
                    if color[node] == 0:
                        color[neigh] = 1
                    elif color[node] == 1:
                        color[neigh] = 0
                    if not dfs(neigh):
                        return False
                elif color[neigh] == color[node]:
                    return False
            return True
        
        for node in range(1, n + 1):
            if color[node] == -1:
                color[node] = 0
                if not dfs(node):
                    return False
        return True