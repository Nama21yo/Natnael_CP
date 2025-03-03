# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1
        for i in range(n - 2, -1, -1):
            if goal - i <= nums[i]:
                goal = i
        return goal == 0