# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:  
    def runningSum(self, nums: List[int]) -> List[int]:  
        n = len(nums)  
        prefixSum = [0] * n  
        prefixSum[0] = nums[0]  

        for i in range(1, n):  
            prefixSum[i] = prefixSum[i - 1] + nums[i]  
        
        return prefixSum