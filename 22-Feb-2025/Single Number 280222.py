# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        odd_num = nums[0]

        for i in range(1, len(nums)):
            odd_num = odd_num ^ nums[i]
        
        return odd_num

        