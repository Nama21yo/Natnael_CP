# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Optimized to O(n) TC
        pairs = defaultdict(int)
        n = len(nums)
        count = 0
        for i in range(n):
            pairs[nums[i]] += 1
        
        for key, value in pairs.items():
            if value >= 2:
                count += (value) * (value - 1) // 2
        
        return count
        