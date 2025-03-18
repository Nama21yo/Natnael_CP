# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        count_ones = 0
        for char in s:
            if char == "1":
                count_ones += 1
        ans = ["0"]*n
        for i in range(count_ones - 1):
            ans[i] = "1"
        ans[n - 1] = "1"
        return "".join(ans)