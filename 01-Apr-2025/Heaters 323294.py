# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        l = 0
        r = max(houses[-1] , heaters[-1])
        ans = 0
        def feasible(radius):
            i = 0
            j = 0
            while i < len(houses) and j < len(heaters):
                if abs(houses[i] - heaters[j]) <= radius:
                    i += 1
                else:
                    j += 1
            return i == len(houses) 
        while l <= r:
            mid = l + (r - l) // 2
            if feasible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans