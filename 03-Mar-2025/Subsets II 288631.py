# Problem: Subsets II - https://leetcode.com/problems/subsets-ii/

class Solution:
    # Using Bit Manipulation
    def filter(self, n, nums):
        subset = []
        j = 0
        while n > 0:
            last_bit = (n & 1)
            if last_bit == 1:
                subset.append(nums[j])
            j += 1
            n = n >> 1
        return subset
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # to ensure that duplicate elements are adjacent
        n = len(nums)
        subsets = set()
        for i in range(1<<n):
            subset = self.filter(i, nums)
            subsets.add(tuple(subset))
        
        return [list(subset) for subset in subsets]