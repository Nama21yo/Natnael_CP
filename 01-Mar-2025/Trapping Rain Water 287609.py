# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        prev_greater = [0] * n
        next_greater = [0] * n
        # Compute Previous Greater Element (left max)
        prev_max = 0
        for i in range(n):
            prev_max = max(prev_max, height[i])
            prev_greater[i] = prev_max
        # Compute Next Greater Element (right max)
        next_max = 0
        for i in range(n - 1, -1, -1):
            next_max = max(next_max, height[i])
            next_greater[i] = next_max
        # Compute trapped water
        trapped_water = 0
        for i in range(n):
            trapped_water += min(prev_greater[i], next_greater[i]) - height[i]
        return trapped_water
