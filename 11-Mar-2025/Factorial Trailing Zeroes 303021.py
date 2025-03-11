# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Base case: if n is 0, there are no trailing zeros in 0!
        # Return 0 for n = 0
        if n == 0:
            return 0
        
        # Recursive case:
        # 1. Divide n by 5 to count the number of multiples of 5 in n.
        # 2. Recursively call trailingZeroes(n // 5) to account for
        #    higher powers of 5 (like 25, 125, etc.) which contribute more trailing zeros.
        return n // 5 + self.trailingZeroes(n // 5)

# Time Complexity:
# - Each recursive call reduces `n` by a factor of 5.
# - The number of recursive calls is proportional to log base 5 of n (i.e., O(log₅(n))).
# - In terms of Big-O, this is equivalent to O(log(n)) as constants like the base of logarithms are ignored.
