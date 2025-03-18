# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(c**0.5)
        print(r)
        while l <= r:
            sumi = (l * l) + (r * r)
            if sumi == c:
                return True
            elif sumi > c:
                r -= 1
            else:
                l += 1
        return False