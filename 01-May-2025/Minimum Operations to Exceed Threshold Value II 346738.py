# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        operations = 0
        while nums and nums[0] < k:
            if len(nums) < 2:
                return -1
            first = heappop(nums)
            second = heappop(nums)
            inserted_el = first * 2 + second
            heappush(nums, inserted_el)
            operations += 1
        return operations


