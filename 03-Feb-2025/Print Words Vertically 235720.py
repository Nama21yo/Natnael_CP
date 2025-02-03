# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        # s = s.strip()
        split_space = s.split()
        maxi = 0
        for string in split_space:
            maxi = max(maxi, len(string))
        
        ans = []
        m = 0
        for i in range(maxi):
            helper = []
            for j in range(len(split_space)):
                if i >= len(split_space[j]):
                    helper.append(" ")
                else:
                    helper.append(split_space[j][i])
            ans.append("".join(helper).rstrip())
        return ans

        