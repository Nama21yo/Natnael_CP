# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = ["", "", "abc", "def", "ghi","jkl","mno","pqrs","tuv","wxyz"]
        comb = []
        if len(digits) == 0:
            return []
        def backtrack(path, i):
            if i == len(digits):
                comb.append("".join(path))
                return
            
            num = int(digits[i])
            for j in range(len(keypad[num])):
                path.append(keypad[num][j])
                backtrack(path, i + 1)
                path.pop()
        backtrack([], 0)
        return comb
        