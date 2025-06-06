# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    # Using Bit Manipulation
    def filter(self, n, nums):
        subset = []
        j = len(nums) - 1
        while n > 0:
            last_bit = (n & 1)
            if last_bit == 1:
                subset.append(nums[j])
            j -= 1
            n = n >> 1
        return subset
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = set()
        for i in range(1<<n):
            subset = self.filter(i, nums)
            subsets.add(tuple(subset))
        
        return [list(subset) for subset in subsets]