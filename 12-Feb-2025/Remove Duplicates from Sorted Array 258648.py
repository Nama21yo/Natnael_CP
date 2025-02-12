# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0  
        for r in range(1, n):
            if nums[l] != nums[r]:
                l += 1
                nums[l], nums[r] = nums[r], nums[l]
        return l + 1