# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ancestor_set = [set() for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
        
        indegrees = [0] * n

        for node in range(n):
            for neigh in graph[node]:
                indegrees[neigh] += 1
                ancestor_set[neigh].add(node)
        
        queue = deque( [node for node in range(n) if indegrees[node] == 0])

        order = []
        while queue:
            node = queue.popleft()
            order.append(node)

            for neigh in graph[node]:
                indegrees[neigh] -= 1
                if indegrees[neigh] == 0:
                    queue.append(neigh)
        
        # add other ancestors other than the immediate parent
        for node in order:
            for neigh in graph[node]:
                ancestor_set[neigh].update(ancestor_set[node])
        
        ancestor_list = [[] for _ in range(n)]
        for i in range(n):
            for node in range(n):
                # skip if the node is the same as itself. A node shouldn't be its own ancestor.
                if node == i:
                    continue
                if node in ancestor_set[i]:
                    ancestor_list[i].append(node)
        return ancestor_list

                



        