# Problem: Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def findPivot(self, nums):
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            mid = l + (r - l) // 2
            if mid < r and nums[mid] > nums[mid + 1]:
                return mid + 1
            elif mid > l and nums[mid] < nums[mid - 1]:
                return mid
            elif nums[mid] >= nums[l]:
                l = mid + 1
            elif nums[l] > nums[mid]:
                r = mid - 1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot = self.findPivot(nums)
        if pivot == -1:
            idx = bisect_left(nums,target) # search the entire array
            if idx < n and nums[idx] == target:
                return idx
        else:
            idx = bisect_left(nums, target, 0, pivot - 1)
            if idx < pivot and nums[idx] == target:
                return idx
            idx = bisect_left(nums, target, pivot , n)
            if idx < n and nums[idx] == target:
                return idx
        return - 1