# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        stack = []
        temp = float("-inf")
        for i in range(n - 1,-1,-1):
            if nums[i] < temp:
                return True
            
            while stack and stack[-1] < nums[i]:
                temp = stack.pop()
            stack.append(nums[i])
        return False
        
        