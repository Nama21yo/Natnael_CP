# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2 ** n - 1
        def helper(length, k):
            # base case
            if length == 1:
                return "0"
            half = length // 2
            if k <= half: # left side
                return helper(half, k)
            elif k > half + 1: # right side
                res = helper(half, (length - k) + 1)
                return "0" if res == "1" else "1"
            else: # the middle
                return "1"
        return helper(length, k)
        