# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller_el = 0
        larger_el = 0
        n = len(nums)

        for num in nums:
            if num < target:
                smaller_el += 1
            elif num > target:
                larger_el += 1

        return list(range(smaller_el, n - larger_el))

        