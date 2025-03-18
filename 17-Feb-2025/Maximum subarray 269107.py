# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        # some inversion of prefixSum
        max_so_far = nums[0] 

        max_ending = 0

        for num in nums:
            max_ending += num
            if max_so_far < max_ending:
                max_so_far = max_ending
            if max_ending < 0:
                max_ending = 0
        
        return max_so_far

        