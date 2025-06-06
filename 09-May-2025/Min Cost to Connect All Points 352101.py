# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        graph = {i : [] for i in range(n)} # i : [cost , node]

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append([dist, j])
                graph[j].append([dist, i])
        
        
        # prim's
        res = 0
        visit = set()
        minHeap = [[0, 0]]
        while len(visit) < n:
            cost , i = heappop(minHeap)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neighCost, neigh in graph[i]:
                if neigh not in visit:
                    heappush(minHeap, [neighCost, neigh])
        return res