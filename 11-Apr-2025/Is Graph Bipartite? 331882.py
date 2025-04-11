# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1 for _ in range(n)]
        def dfs(node):
            each_check = True
            for neigh in graph[node]:
                if color[neigh] == -1:
                    if color[node] == 0:
                        color[neigh] = 1
                    elif color[node] == 1:
                        color[neigh] = 0
                    each_check = each_check and dfs(neigh)
                elif color[neigh] == color[node]:
                    return False
            return each_check
        
        is_bipartite = True
        for node in range(n):
            if color[node] == -1:
                color[node] = 0
                is_bipartite = is_bipartite and dfs(node)
        return is_bipartite