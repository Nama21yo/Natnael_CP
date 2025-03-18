# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumCount = defaultdict(int)
        prefixSumCount[0] = 1
        prefixSum = 0
        count = 0
        for num in nums:
            prefixSum += num
            
            count += prefixSumCount[prefixSum - k]
            
            prefixSumCount[prefixSum] = prefixSumCount[prefixSum] + 1
        
        return count