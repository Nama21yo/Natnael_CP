# Problem: Number of Ways to Reach a Position After Exactly k Steps - https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        
        gap = abs(endPos-startPos)
        leftover = k - gap
        return 0 if leftover % 2 != 0 or leftover < 0 else math.comb(k, int(leftover/2)) % (10**9 + 7)