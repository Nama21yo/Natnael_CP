# Problem: Largest Rectangle in Histogram (Optional) - https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # just span as leet 5 - longest pal substring
        # find the previous smaller
        n = len(heights)
        previous_smaller = [-1] * n  
        # n is used here to indicate no smaller element exists to the right
        next_smaller = [n] * n # remember it should be n rather than -1
        stack = []
        for i in range(n): # left
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                previous_smaller[i] = stack[-1] # put the index
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1, -1):# right
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(i)
        
        # width >> r - l - 1
        # height >> current height
        max_area = -1
        for i in range(n):
            width =  next_smaller[i] - previous_smaller[i] - 1
            height = heights[i]
            curr_area = width * height
            max_area = max(max_area, curr_area)
        return max_area

