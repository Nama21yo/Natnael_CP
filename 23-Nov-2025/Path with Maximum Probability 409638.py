# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = {i : [] for i in range(n)}
        for (u,v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        
        probs = [0.0] * n
        max_heap = [(-1, start_node)]

        while max_heap:
            current_prob, node = heapq.heappop(max_heap)
            current_prob = - current_prob # change it to +ve

            if node == end_node:
                return current_prob
            
            for neigh, neigh_prob in graph[node]:
                new_prob = neigh_prob * current_prob
                if new_prob > probs[neigh]:
                    probs[neigh] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neigh)) # inorder to use it as max_heap change it to -ve
        return 0.0
                