# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffle_string = list(s)
        n = len(shuffle_string)
        for i in range(n):
            val = indices[i]
            shuffle_string[val]  = s[i]
        return "".join(shuffle_string)