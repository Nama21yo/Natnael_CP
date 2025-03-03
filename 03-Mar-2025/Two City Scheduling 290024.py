# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key= lambda x: x[1] - x[0])
        n = len(costs)
        a_min = 0
        b_min = 0
        # 2n people >> n of a + n of b
        for i in range(n//2):
            b_min += costs[i][1]
        for i in range(n//2, n):
            a_min += costs[i][0]
        return a_min + b_min