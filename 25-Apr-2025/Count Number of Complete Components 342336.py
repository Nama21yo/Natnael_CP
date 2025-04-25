# Problem: Count Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(graph, node, visited, nodes, edge_count):
            visited.add(node)
            nodes.append(node)
            for neigh in graph[node]:
                edge_count[0] += 1
                if neigh not in visited:
                    dfs(graph, neigh, visited, nodes, edge_count)
        visited = set()
        comp_component = 0
        for i in range(n):
            if i not in visited:
                nodes = []
                edge_count = [0]
                dfs(graph, i, visited, nodes, edge_count)
                num_nodes = len(nodes)
                actual_edges = edge_count[0] // 2  # because each edge is counted twice
                if actual_edges == (num_nodes * (num_nodes - 1)) // 2:
                    comp_component += 1

        return comp_component
