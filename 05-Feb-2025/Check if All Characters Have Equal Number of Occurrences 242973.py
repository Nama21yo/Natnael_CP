# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count_good = Counter(s)
        first_count = count_good[s[0]]
        
        for count in count_good.values():
            if count != first_count:
                return False
        return True
        