# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapify(stones)
        while len(stones) > 1:
            max_ = heappop(stones)
            max__ = heappop(stones)
            if max_ != max__:
                inserted = -max_ - (-max__)
                heappush(stones, -inserted)
        return -stones[0] if len(stones) == 1 else 0