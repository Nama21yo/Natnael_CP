# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def subsequence(nums, i, output):
            if i == len(nums):
                # since it is pass by reference copy it
                ans.append(output.copy())
                return
            # include
            output.append(nums[i])
            subsequence(nums, i + 1, output)
            # exclude while backtracking
            output.pop()
            subsequence(nums, i + 1, output)
        subsequence(nums, 0, [])
        return ans