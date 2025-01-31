# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = len(s) -1

        while s[last] == " ":
            # start from last and move to the last word that isn't space
            last -= 1
        first = last
        while first >= 0 and s[first] != " ":
            first -= 1
        return last - first

