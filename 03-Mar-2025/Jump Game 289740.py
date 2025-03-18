# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest_d = 0
        for i in range(n):
            if farthest_d < i: # won't work for last index 3 < 4
                return False
            farthest_d = max(i + nums[i], farthest_d)
        return True