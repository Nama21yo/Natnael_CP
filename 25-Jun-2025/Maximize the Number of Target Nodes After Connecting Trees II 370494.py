# Problem: Maximize the Number of Target Nodes After Connecting Trees II - https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

class Solution:
    def buildGraph(self, edges, size):
        graph = [[] for _ in range(size)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def bfs(self, graph):
        n = len(graph)
        color_count = [0, 0]
        node_color = [0] * n
        visited = [False] * n
        queue = deque([(0, 0)])
        visited[0] = True

        while queue:
            node, color = queue.popleft()
            node_color[node] = color
            color_count[color] += 1

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, 1 - color))

        return color_count, node_color

    def maxTargetNodes(self, edges1, edges2):
        n = len(edges1) + 1
        m = len(edges2) + 1

        tree1 = self.buildGraph(edges1, n)
        tree2 = self.buildGraph(edges2, m)

        color1, node_color1 = self.bfs(tree1)
        color2, _ = self.bfs(tree2)

        max_color2 = max(color2)

        result = [0] * n
        for i in range(n):
            result[i] = color1[node_color1[i]] + max_color2

        return result