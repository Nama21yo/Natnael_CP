# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:  
    def runningSum(self, nums: List[int]) -> List[int]:  
        n = len(nums)  
        running_sum = 0
        ans = []
        for i in range(n):  
            running_sum += nums[i]
            ans.append(running_sum)

        return ans