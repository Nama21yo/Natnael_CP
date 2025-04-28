# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total = sum(piles)
        piles = [-x for x in piles]
        heapify(piles) # in place
        for i in range(k):
            max_ = -1 * heappop(piles)
            removed = (max_ // 2)
            total = total - removed
            heappush(piles, (-1 * (max_ - removed)))
        return total