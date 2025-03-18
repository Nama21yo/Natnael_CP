# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ = [0]*26
        
        for i,char in enumerate(s):
            last_occ[ord(char) - ord("a")] = i
        n = len(s)
        start = 0
        end = 0
        ans = []
        for i in range(n):
            end = max(end, last_occ[ord(s[i]) - ord("a")])
            # match it with merge intervals
            if end == i:
                ans.append(end - start + 1)
                start = i + 1
        return ans
