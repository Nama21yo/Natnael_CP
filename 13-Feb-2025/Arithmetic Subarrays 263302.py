# Problem: Arithmetic Subarrays - https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def sort_range(self,arr, start, end):
        return sorted(arr[start:end])
    def check_arthimetic(self,nums):
        n = len(nums)
        diff = nums[1] - nums[0]
        for i in range(2,n):
            if nums[i] - nums[i - 1] != diff:
                return False
        return True
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        arth_range =list(zip(l,r))
        ans = []
        for left, right in arth_range:
            sorted_range = self.sort_range(nums, left, right + 1)
            ans.append(self.check_arthimetic(sorted_range))
        return ans

