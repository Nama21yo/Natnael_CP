# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
         # Calculate the initial gap
        gap = math.ceil((m + n) / 2)

        def swap_elements(left, right):
            """Helper function to swap elements if needed."""
            if left < m and right >= m:
                if nums1[left] > nums2[right - m]:
                    nums1[left], nums2[right - m] = nums2[right - m], nums1[left]
            elif left >= m:
                if nums2[left - m] > nums2[right - m]:
                    nums2[left - m], nums2[right - m] = nums2[right - m], nums2[left - m]
            else:
                if nums1[left] > nums1[right]:
                    nums1[left], nums1[right] = nums1[right], nums1[left]

        while gap > 0:
            left = 0
            right = left + gap

            while right < (m + n):
                swap_elements(left, right)
                left += 1
                right += 1

            # Recalculate the gap for the next iteration
            if gap == 1:
                break
            gap = math.ceil(gap / 2)
        # Finally, merge nums2 into nums1
        nums1[m:] = nums2
        nums1.sort()  # Sort the final nums1 array