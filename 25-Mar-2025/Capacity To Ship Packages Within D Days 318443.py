# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def is_feasible(self, capacity, weights, given_day):
        curr_weight = 0
        days = 1
        for weight in weights:
            curr_weight += weight

            if curr_weight > capacity:
                days += 1
                curr_weight = weight
                if days > given_day:
                    return False
        return True

        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights) - 1
        r = sum(weights) + 1


        while r - l > 1:
            mid = l + (r - l)// 2
            if self.is_feasible(mid, weights, days):
                r = mid
            else:
                l = mid
        
        return l + 1

        
        