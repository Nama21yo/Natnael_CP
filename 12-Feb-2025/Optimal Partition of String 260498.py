# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        set_s = set()
        min_substring = 0
        for char in s:
            if char not in set_s:
                set_s.add(char)
            else:
                min_substring += 1
                set_s = set(char)
        return min_substring + 1
        
                