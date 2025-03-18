# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # merge them starting from the back
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            # since we are starting from the end
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # for the rest
        
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        
        return nums1
        