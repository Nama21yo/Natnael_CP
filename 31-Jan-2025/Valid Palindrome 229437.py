# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pure_alpha = "".join([char.lower() for char in s if char.isalpha() or char.isdigit()])

        reversed_alpha = pure_alpha[::-1]

        return pure_alpha == reversed_alpha
        