# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        max_balanced = 0
        count = 0
        for char in s:
            if char == "R":
                count += 1
            else:
                count -= 1
            if count == 0:
                max_balanced += 1
        return max_balanced