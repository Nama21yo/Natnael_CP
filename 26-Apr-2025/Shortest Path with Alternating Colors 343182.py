# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph = [defaultdict(list) for _ in range(2)]
        for start, end in red_edges:
            graph[0][start].append(end)
        for start, end in blue_edges:
            graph[1][start].append(end)
        distances = [-1] * n
        visited = set()
        queue = deque([(0, 0), (0, 1)])
        distance = 0

        # Iterate until there are no more nodes to visit
        while queue:
            for _ in range(len(queue)):
                node, color = queue.popleft()
                if distances[node] == -1:
                    distances[node] = distance
                visited.add((node, color))
                # Alternate the color for the next edges to consider (0 -> 1 or 1 -> 0)
                color ^= 1
                # Enqueue all the adjacent nodes of the alternated color
                for neighbor in graph[color][node]:
                    if (neighbor, color) not in visited:
                        queue.append((neighbor, color))
            # After exploring the nodes at the current distance, increment for the next level
            distance += 1
        return distances