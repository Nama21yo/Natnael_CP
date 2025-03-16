# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def pow(a, n , mod):
        if n == 0:
            return 1
        if n % 2 == 0:
            return pow((a * a) % mod, n // 2, mod) % mod
        return (pow((a * a) % mod, n // 2, mod) % mod) * a
             
    def countGoodNumbers(self, n: int) -> int:
        # Total Good Numbers = (5^E * 4^O) % (10^9 + 7)
        even = n // 2 if n % 2 == 0 else ((n // 2) + 1)
        odd = n // 2
        counte = pow(5, even, 10 ** 9 + 7)
        counto = pow(4 , odd, 10**9 + 7)

        return (counte * counto) % (10**9 + 7)

        