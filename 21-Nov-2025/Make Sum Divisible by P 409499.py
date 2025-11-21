# Problem: Make Sum Divisible by P - https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rem = total % p

        if rem == 0:
            return 0
        
        res  = len(nums)

        curr_sum = 0
        # map remain of prefix sums to last Index
        map = {0:-1}

        for i , n in enumerate(nums):
            # rem + x = curr_sum
            # x = curr_sum - rem
            curr_sum = (curr_sum + n) % p
            prefix = (curr_sum - rem + p) % p
            
            if prefix in map:
                length = i - map[prefix]
                res = min(res, length)
            
            map[curr_sum] = i


        
        return -1 if res == len(nums)else res
        