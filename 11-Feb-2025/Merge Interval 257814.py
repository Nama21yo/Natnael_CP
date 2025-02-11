# Problem: Merge Interval - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        ans = [intervals[0]]

        for i in range(1,n):
            prev = ans[-1]
            curr = intervals[i]
            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
            else:
                ans.append(curr)
        return ans
