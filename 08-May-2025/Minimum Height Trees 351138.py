# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        # there will be at most 2 nodes that could be minimum
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        edge_count = {}
        leaves = deque()
        for src, neigh in graph.items():
            if len(neigh) == 1: # it is a leaf
                leaves.append(src)
            edge_count[src] = len(neigh)
        
        while leaves:
            if n <= 2: # total number of remaining leaves
                return list(leaves)

            length = len(leaves)
            for i in range(length):
                node = leaves.popleft()
                n -= 1
                for neigh in graph[node]:
                    edge_count[neigh] -= 1
                    if edge_count[neigh] == 1:
                        leaves.append(neigh)