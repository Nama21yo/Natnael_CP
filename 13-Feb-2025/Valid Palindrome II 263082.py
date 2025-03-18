# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def check_rest(self, s, l , r):
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        count_removal = 0

        while l < r:
            if s[l] != s[r]:
                count_removal += 1
                return self.check_rest(s,l, r - 1) or self.check_rest(s,l+1, r)
            else:
                l += 1
                r -= 1
        return count_removal <= 1