# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]

        while left <= right:
            if left_max <= right_max:
                trapped_water += left_max - height[left]
                left += 1
                if left < len(height):  # Check to prevent out-of-bounds error
                    left_max = max(left_max, height[left])
            else:
                trapped_water += right_max - height[right]
                right -= 1
                if right >= 0:  # Check to prevent out-of-bounds error
                    right_max = max(right_max, height[right])

        return trapped_water
