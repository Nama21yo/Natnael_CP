# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_map = defaultdict(int)
        prefix_map[0] = 1

        running_sum = 0
        count_subarray = 0
        for num in nums:
            running_sum += num

            target = running_sum % k
            if target in prefix_map:
                count_subarray += prefix_map[target]
            
            prefix_map[target] += 1
        return count_subarray