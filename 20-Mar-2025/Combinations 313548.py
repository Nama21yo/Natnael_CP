# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combination = []
        def backtrack(i,path):
            if len(path) == k:
                combination.append(path[:])
                return
            max_iteration = n - ((k - len(path))) + 1 # pruning
            for candidate in range(i, max_iteration + 1):
                path.append(candidate)
                backtrack(candidate + 1, path)
                path.pop()
        backtrack(1, [])
        return combination