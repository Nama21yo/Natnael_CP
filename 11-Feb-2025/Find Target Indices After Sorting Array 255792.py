# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def first_occ_binary_search(self, nums, target):
        first = -1
        l = 0
        n = len(nums)
        r = n - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                first = mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return first
    
    def last_occ_binary_search(self, nums,target):
        last = -1
        l = 0
        n = len(nums)
        r = n - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                last = mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return last
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        first_occ = self.first_occ_binary_search(nums, target)
        if first_occ == -1:
            return []
        last_occ = self.last_occ_binary_search(nums, target)
        if last_occ == -1:
            return []
        
        return list(range(first_occ, last_occ + 1))

        