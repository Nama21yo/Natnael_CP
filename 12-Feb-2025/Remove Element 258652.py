# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        l = 0
        # /remember the quick sort partition 
        for r in range(n):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l 
        