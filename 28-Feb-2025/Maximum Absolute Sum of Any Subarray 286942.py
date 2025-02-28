# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # max of max sum and min sum
        max_so_far = float("-inf")
        max_ending = 0

        min_so_far = 0
        min_ending = 0

        for num in nums:
            max_ending += num

            min_ending += num
            min_so_far = min(min_so_far, min_ending)

            if max_ending > max_so_far:
                max_so_far = max_ending
            
            min_ending = min(min_ending, 0)
            if max_ending < 0:
                max_ending = 0
        return max(max_so_far, abs(min_so_far))