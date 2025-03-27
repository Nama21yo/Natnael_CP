# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repair(mid):
            repaired = 0
            for rank in ranks:
                repaired += floor(sqrt(mid / rank) )
            return repaired >= cars
        l = 0
        r = 10**14
        while r - l > 1:
            mid = l + (r  - l) // 2
            if can_repair(mid):
                r = mid
            else:
                l = mid
        return r