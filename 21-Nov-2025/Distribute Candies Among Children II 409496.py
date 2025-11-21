# Problem: Distribute Candies Among Children II - https://leetcode.com/problems/distribute-candies-among-children-ii/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def comb(a, b):
            if a < b or a < 0: 
                return 0
            return math.comb(a, b)

        ans = comb(n + 2, 2)
        ans -= 3 * comb(n - limit + 1, 2)
        ans += 3 * comb(n - 2 * limit, 2)
        ans -= comb(n - 3 * limit - 1, 2)
        
        return ans
