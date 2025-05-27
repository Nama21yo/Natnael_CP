# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(s, path, output):
            if not s:
                output.append("".join(path))
                return
            
            if s[0].isalpha():
                path = path + [s[0].lower()]
                backtrack(s[1:], path, output)
                path.pop()
                path =  path + [s[0].upper()]
                backtrack(s[1:], path, output)
                # path.pop()
            else:
                backtrack(s[1:], path + [s[0]] , output)
        output = []
        backtrack(s, [], output)
        return output