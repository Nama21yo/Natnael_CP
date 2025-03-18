# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Base case: if n is less than 1, it cannot be a power of two
        if n < 1:
            return False
        # Base case: if n is exactly 1, it is a power of two
        if n == 1:
            return True
        # Recursive case: if n is divisible by 2, continue checking with n divided by 2
        if n % 2 == 0:
            return self.isPowerOfTwo(n // 2)
        # If n is not divisible by 2, it cannot be a power of two
        return False
