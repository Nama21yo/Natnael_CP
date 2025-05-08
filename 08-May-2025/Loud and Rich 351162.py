# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        for u,v in richer:
            graph[v].append(u)
        # TC and SC - O(V + E)
        output = [None for i in range(n)]
        def dfs(graph, source, quietness, output):
            least_quiet = source
            for neigh in graph[source]:
                if output[neigh] is None:
                    dfs(graph, neigh, quietness, output)
                least_quiet = min(least_quiet, output[neigh], key=lambda x : quietness[x])
            output[source] = least_quiet
        for person in range(n):
            if output[person] is None:
                dfs(graph, person, quiet, output)
        return output