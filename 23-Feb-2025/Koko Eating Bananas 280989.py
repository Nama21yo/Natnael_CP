# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles, h):
        low, high = 1, max(piles)
        
        while low < high:
            mid = low + (high - low) // 2
            if self.isPossible(piles, h, mid):
                high = mid
            else:
                low = mid + 1
                
        return low
    
    def isPossible(self, piles, h, speed):
        totalHours = 0
        for pile in piles:
            totalHours += (pile + speed - 1) // speed
        return totalHours <= h
