# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        # reverse the graph
        reversed_graph = [[] for _ in range(n)]
        for node in range(n):
            for neigh in graph[node]:
                reversed_graph[neigh].append(node)
        
        indegrees = [0] * n

        for node in range(n):
            for neigh in reversed_graph[node]:
                indegrees[neigh] += 1

        safe_states = []
        queue = deque([node for node in range(n) if indegrees[node] == 0])

        while queue:
            node = queue.popleft()
            safe_states.append(node)

            for neigh in reversed_graph[node]:
                indegrees[neigh] -= 1
                if indegrees[neigh] == 0:
                    queue.append(neigh)
                
        return sorted(safe_states)