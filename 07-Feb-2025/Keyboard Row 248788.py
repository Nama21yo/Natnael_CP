# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        ans = []

        for word in words:

            lower_word = set(word.lower())

            # The issubset() method returns True if all items in the set exists in the 
            # specified set, otherwise it returns False.

            # As a shortcut, you can use the <= operator instead

            if lower_word <= row1 or lower_word <= row2 or lower_word <= row3:
                ans.append(word)
        
        return ans