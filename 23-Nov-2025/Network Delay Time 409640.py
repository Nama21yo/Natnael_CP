# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i : [] for i in range(1, n + 1)}
        for u,v,w in times:
            graph[u].append((v,w))

        # dijkstra algorithm here
        distances = { node: float("inf") for node in graph}
        distances[k] = 0
        processed = set()
        min_heap = [(0, k)]

        while min_heap:
            current_dist, current_node = heapq.heappop(min_heap)

            if current_node in processed:
                continue
            processed.add(current_node)

            for neigh, weight in graph[current_node]:
                distance = current_dist + weight
                if distance < distances[neigh]:
                    distances[neigh] = distance
                    heapq.heappush(min_heap, (distance, neigh))
        
        max_dist = max(distances.values())

        return max_dist if max_dist < float("inf") else -1