# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        count_good = 0

        running_sum = 0

        for num in nums:
            # put odds as 1 and even as 0
            running_sum += num % 2
            target = running_sum - k

            if target in prefix_map:
                count_good += prefix_map[target]
            prefix_map[running_sum] += 1
        return count_good

            