# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def permutations(path, i):
            # base case
            if i == len(path) - 1:
                ans.append(path[:])
                return
            # rec case
            for j in range(i , len(path)):
                path[i], path[j] = path[j], path[i]
                permutations(path, i + 1)
                path[i], path[j] = path[j], path[i]
        permutations(nums, 0)
        return ans