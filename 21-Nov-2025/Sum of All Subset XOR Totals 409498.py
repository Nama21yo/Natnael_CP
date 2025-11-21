# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        or_all = 0
        for v in nums:
            or_all |= v
            
        return or_all * (1 << (n - 1))