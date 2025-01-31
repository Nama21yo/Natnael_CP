# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        full_iteration = time // (n - 1)

        back_iteration = time % (n - 1)

        if full_iteration % 2 == 0:
            return back_iteration + 1 
        else:
            return n - back_iteration  