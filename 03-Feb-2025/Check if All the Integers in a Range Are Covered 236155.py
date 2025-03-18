# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # Line Sweep Algorithm
        count_interval = [0] * 100
        for interval in ranges:
            count_interval[interval[0]] += 1
            count_interval[interval[1] + 1] -= 1
        
        prefix_sum = [0]*51
        prefix_sum[0] = count_interval[0]

        for i in range(1,51):
            prefix_sum[i] = prefix_sum[i - 1] + count_interval[i]


        for i in range(left, right + 1):
            if prefix_sum[i] <= 0:
                return False
        return True


        