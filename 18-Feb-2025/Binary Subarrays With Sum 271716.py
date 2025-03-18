# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_map = defaultdict(int)
        prefix_map[0] = 1

        running_sum = 0
        count_subarray = 0
        for num in nums:
            running_sum += num
            target = running_sum - goal
            if target in prefix_map:
                count_subarray += prefix_map[target]
            
            # if target not in prefix_map:
            prefix_map[running_sum] += 1
        return count_subarray