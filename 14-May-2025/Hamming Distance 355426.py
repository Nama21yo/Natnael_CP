# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        while x > 0 or y > 0:
            last_1 = x & 1
            last_2 = y & 1
            if last_1 != last_2:
                dist += 1
            x >>= 1
            y >>= 1
        return dist