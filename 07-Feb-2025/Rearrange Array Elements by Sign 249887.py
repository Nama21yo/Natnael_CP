# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Separate positive and negative numbers
        positives = [num for num in nums if num >= 0]
        negatives = [num for num in nums if num < 0]
        
        # Interleave positive and negative numbers
        return [positives[i//2] if i % 2 == 0 else negatives[i//2] for i in range(len(nums))]
