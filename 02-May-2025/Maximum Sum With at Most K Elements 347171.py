# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        heap = []
        for r in range(rows):
            row_col = [-num for num in grid[r]]
            heapify(row_col)
            for _ in range(limits[r]):
                heap.append(heappop(row_col))
        heapify(heap)
        ans = sum([-heappop(heap) for i in range(k)])
        return ans
            
