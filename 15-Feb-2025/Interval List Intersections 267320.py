# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n = len(firstList)
        m = len(secondList)

        l = 0
        r = 0
        intersection = []
        while l < n and r < m:
            start_a, end_a = firstList[l]
            start_b, end_b = secondList[r]
            # intersect them if they have intersecction
            if start_a <= end_b and end_a >= start_b:
                # take the maximum of left and minimum of right
                intersection.append([max(start_a, start_b),min(end_a, end_b)])
            
            if end_a <= end_b:
                l += 1
            else:
                r += 1
        return intersection
