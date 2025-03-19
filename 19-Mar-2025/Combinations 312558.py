# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        def backtrack(i,path):
            if len(path) == k:
                combinations.append(path[:])
                return
            if i > n:
                return
            # pick the current one
            path.append(i)
            backtrack(i + 1, path)
            # don't pick it
            path.pop()
            backtrack(i + 1, path)
        
        backtrack(1, [])
        return combinations
