# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def josephus(n, k):
            if (n == 1):
                return 1
            else:
                return (josephus(n - 1, k) + k-1) % n + 1
        return josephus(n,k)
