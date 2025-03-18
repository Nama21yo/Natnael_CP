# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        operations = 0
        while target > 1:
            if target % 2 == 0 and maxDoubles > 0:
                target = target // 2
                maxDoubles -= 1
                operations += 1
            else:
                if maxDoubles == 0:
                    operations += target - 1
                    break # or make target = 1
                else:
                    target -= 1
                    operations += 1
        return operations