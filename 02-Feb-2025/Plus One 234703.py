# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Traverse from the last index
        n = len(digits) 
        for i in range(n - 1, -1, -1):
            # if the last digit isn't 9
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            
            # if the last digit is 9
            digits[i] = 0
        return [1] + digits