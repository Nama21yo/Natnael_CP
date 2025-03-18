# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n == 0:
                return 1  
            #Example-   2 ^ 3 = (2)^ 2 * 2 = (2 * 2) ^ 1 
            if n % 2 == 0: 
                return helper(x * x, n // 2)
            # for odd just decrement it 
            return x * (helper(x, n - 1) )
        if n < 0:
            x = 1 / x
            n = -n
        return helper(x, n)