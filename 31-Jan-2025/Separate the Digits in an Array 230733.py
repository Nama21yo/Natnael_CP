# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def each_digits(self, n):
        each_digit = []
        while n > 0:
            each_digit.append(n % 10)
            n  //= 10
        each_digit.reverse()
        return each_digit
    def separateDigits(self, nums: List[int]) -> List[int]:
        sep_digits = []
        for num in nums:
            current_digit = self.each_digits(num)
            sep_digits.extend(current_digit)
        # sep_digits.sort()
        return sep_digits

        