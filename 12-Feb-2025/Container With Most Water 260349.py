# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # . All pairs of the n lines define a rectangle with a height given by the 
        # shorter line and a width given by the distance between the lines. Return 
        # the area of the rectangle with the largest area

        l = 0
        r = len(height) - 1
        max_area = 0
        while l <= r:
            # length -> min of the two
            # width -> there difference
            current_area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, current_area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area