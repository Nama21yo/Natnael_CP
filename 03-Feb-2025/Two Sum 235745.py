# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums, target):
        map = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in map:
                return [map[diff], i]
            
            map[num] = i
            
        return None
