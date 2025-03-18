# Problem: Minimize Maximum Pair Sum in Array - https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        max_sum = 0

        nums.sort()
        n = len(nums)
        for i in range(n//2):
            max_sum = max(max_sum, nums[i] + nums[n - i - 1])
        return max_sum

