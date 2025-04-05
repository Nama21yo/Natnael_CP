# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def merge(self, nums1, nums2, count_ans):
        n = len(nums1)
        m = len(nums2)
        i = j = 0
        right_smaller = 0
        merged = []
        while i < n and j  < m:
            if nums1[i][0] <= nums2[j][0]:
                merged.append(nums1[i])
                count_ans[nums1[i][1]] += right_smaller
                i += 1
            else:
                right_smaller += 1
                merged.append(nums2[j])
                j += 1
        while i < n:
            count_ans[nums1[i][1]] += right_smaller
            merged.append(nums1[i])
            i += 1
        while j < m:
            merged.append(nums2[j])
            j += 1
        return merged
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums =  [(num, i) for i, num in enumerate(nums)]
        count_ans = [0] * len(nums)
        def mergeSort(nums, left, right, count_ans):
            if left < right:
                mid = left + (right - left) // 2
                left_half = mergeSort(nums, left, mid, count_ans)
                right_half = mergeSort(nums, mid + 1, right, count_ans)
                return self.merge(left_half, right_half, count_ans)
            return [nums[left]]
        mergeSort(nums, 0, len(nums) - 1, count_ans)
        return count_ans

        
        