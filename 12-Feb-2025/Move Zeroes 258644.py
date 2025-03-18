# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = -1
        for r in range(len(nums)):
            if(nums[r] != 0):
                l += 1
                nums[l], nums[r] = nums[r], nums[l]
    
        