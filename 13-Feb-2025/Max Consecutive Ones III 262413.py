# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        zeros  = 0
        max_consecutive = 0 
        for r in range(n):
            if nums[r] == 0:
                zeros += 1
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                max_consecutive = max(max_consecutive, r - l + 1)
        return max_consecutive
        