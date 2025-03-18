# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def expand(self, s, p1, p2):
        while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
            p1 -= 1
            p2 += 1
        return p2 - p1 - 1

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        # O(n ^ 2)
        max_len = 0
        start = 0  
        for i in range(n):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i + 1)
            max_len_current = max(len1, len2)
            if max_len_current > max_len:
                max_len = max_len_current
                start = i - (max_len - 1) // 2
        return s[start:start + max_len]
