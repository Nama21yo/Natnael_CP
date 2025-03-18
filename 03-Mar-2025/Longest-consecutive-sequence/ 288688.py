# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        # O(n), O(n)
        longest_len = 0
        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                x = num + 1
                while x  in num_set:
                    length += 1
                    x = x + 1
                
                longest_len = max(longest_len, length)
        return longest_len
                