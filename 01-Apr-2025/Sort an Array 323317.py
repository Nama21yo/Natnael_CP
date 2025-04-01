# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(0 , len(nums) - 1, nums)
    def mergeSort(self, left, right, nums):
        if left < right:
            mid = (left + right) // 2
            l = self.mergeSort(left, mid, nums)
            r = self.mergeSort(mid + 1, right, nums)
            return self.merge(l, r)
        return [nums[left]]
    def merge(self, nums1, nums2):
        l = r =  0
        nums1.append(float("inf"))
        nums2.append(float("inf"))
        merged = []
        while l < len(nums1) - 1 or r < len(nums2) - 1:
            if nums1[l] <= nums2[r]:
                merged.append(nums1[l])
                l += 1
            else:
                merged.append(nums2[r])
                r += 1
        return merged