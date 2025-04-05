# Problem: Reverse Pairs - https://leetcode.com/problems/reverse-pairs/description/

class Solution:
    def merge(self, nums1, nums2, count):
        n = len(nums1)
        m = len(nums2)
        i = j = 0
        merged = []
        while i < n and j  < m:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        while i < n:
            merged.append(nums1[i])
            i += 1
        while j < m:
            merged.append(nums2[j])
            j += 1
        return merged
    def reversePairs(self, nums: List[int]) -> int:
        count = [0]
        def mergeSort(nums, left, right, count):
            if left < right:
                mid = left + (right -  left) // 2
                left_half = mergeSort(nums, left, mid, count)
                right_half = mergeSort(nums, mid + 1, right, count)
                i = j = 0
                while i < len(left_half) and j < len(right_half):
                    if left_half[i] > 2 * right_half[j]:
                        count[0] += len(left_half) - i
                        j += 1
                    else:
                        i += 1
                return self.merge(left_half, right_half, count)
            return [nums[left]]
        mergeSort(nums, 0, len(nums) - 1, count)
        return count[0]