# Problem: Number of Ways to Select Buildings - https://leetcode.com/problems/number-of-ways-to-select-buildings/

class Solution:
    def numberOfWays(self, s: str) -> int:
        # There are only 2 valid patterns: ‘101’ and ‘010’.

        # If encountering 0 count subsequences ending at 0.
        # no of 10 >> no of 1's before current 0
        # no of 010 >> no of 01's before 0

        # If encountering 1, count subsequences ending at 1.
        # no of 01 >> no of 0's before current 1
        # no of 101 >> no of 10 before current 1 
        ways = 0
        one = zero = zero_one = one_zero = 0
        for c in s:
            if c == '0':
                zero += 1
                one_zero += one
                ways += zero_one
            else:
                one += 1    
                zero_one += zero 
                ways += one_zero
        return ways