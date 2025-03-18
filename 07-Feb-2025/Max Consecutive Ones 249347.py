# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        # Value is known which is one
        for num in nums:
            if num ==  1:
                count += 1
            else:
                count = 0
            ans = max(ans, count)
        
        return ans
        