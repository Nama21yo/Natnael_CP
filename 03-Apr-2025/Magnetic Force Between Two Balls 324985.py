# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        l = 1
        r = max(position)
        position.sort()
        def feasible(force):
            count = 1
            pos = 0
            curr = position[0]
            for i in range(len(position)):
                pos = abs(position[i] -curr)
                if pos > force:
                    count += 1
                    curr = position[i]
            return count >= m
        ans = 0
        while l <= r:
            mid = l + (r - l) // 2
            if feasible(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans + 1