# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def can_eat(self, speed, piles, given_hour):
        curr = 0
        for pile in piles:
            curr += (pile + speed - 1) // speed if speed != 0 else 0
        return curr <= given_hour
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles) + 1

        while r - l > 1:
            mid = l + (r - l) // 2
            if self.can_eat(mid, piles, h):
                r = mid 
            else:
                l = mid
        return l + 1 