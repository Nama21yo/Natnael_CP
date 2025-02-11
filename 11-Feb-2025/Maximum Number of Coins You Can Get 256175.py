# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        bob_pile = len(piles) - 2
        bob_piles = 0
        j = 0
        while j < len(piles)//3:
            bob_piles += piles[bob_pile]
            bob_pile -= 2
            j += 1

        return bob_piles
        

