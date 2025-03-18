# Problem: K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = sorted(points, key = lambda point: (point[0] ** 2 + point[1] ** 2))

        return [points[i] for i in range(k)]