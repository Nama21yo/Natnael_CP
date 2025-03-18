# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # Simulation + moving zeroes pattern(Two pointers)
        n = len(nums)
        # n - 1 operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # move the zeroes to the end
        l = 0
        for r in range(n):
            if nums[r] != 0:
                # swap it with the zero
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
        return nums