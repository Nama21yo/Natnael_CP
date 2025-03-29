# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l = 0
        r = max(candies) + 1
        def feasible(mid):
            count = 0
            for candy in candies:
                count += (candy // mid)
            return count >= k
        while r - l > 1:
            mid = l + (r - l) // 2
            if feasible(mid):
                l = mid
            else:
                r = mid 
        return l
