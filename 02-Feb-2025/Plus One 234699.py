# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits))
        num = int("".join(digits))
        plus_one = str(num + 1)
        return  list(map(int,plus_one))
        