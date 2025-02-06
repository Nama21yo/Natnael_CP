# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count_allowed = Counter(allowed)

        count_consistent = 0

        for word in words:
            flag = False
            for char in word:
                if count_allowed[char] == 0:
                    flag = True
                    break
            count_consistent += 1 if not flag else 0
        
        return count_consistent