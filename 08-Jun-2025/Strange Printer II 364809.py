# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/


class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        n, m = len(targetGrid), len(targetGrid[0])
        boundaries = defaultdict(lambda : [float('inf'), -1, float('inf'), -1])  # left, right, top, bottom

        #  Find boundaries for each color
        for r in range(n):
            for c in range(m):
                color = targetGrid[r][c]
                boundaries[color][0] = min(boundaries[color][0], c)  # left
                boundaries[color][1] = max(boundaries[color][1], c)  # right
                boundaries[color][2] = min(boundaries[color][2], r)  # top
                boundaries[color][3] = max(boundaries[color][3], r)  # bottom

        # Build the graph of dependencies
        graph = defaultdict(set)
        incoming = defaultdict(int)

        for color in boundaries:
            left, right, top, bottom = boundaries[color]
            for r in range(top, bottom + 1):
                for c in range(left, right + 1):
                    other_color = targetGrid[r][c]
                    if other_color != color and other_color not in graph[color]:
                        graph[color].add(other_color)
                        incoming[other_color] += 1

        # Topological Sort (Kahn’s Algorithm)
        q = deque()
        for color in boundaries:
            if incoming[color] == 0:
                q.append(color)

        processed = 0
        while q:
            node = q.popleft()
            processed += 1
            for nei in graph[node]:
                incoming[nei] -= 1
                if incoming[nei] == 0:
                    q.append(nei)

        return processed == len(boundaries)