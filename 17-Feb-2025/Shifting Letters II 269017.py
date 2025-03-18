# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shifting_prefix = [0]*(n + 1)

        for start,end,direction in shifts:
            if direction == 1:
                shifting_prefix[start] += 1
                shifting_prefix[end + 1] -= 1
            else:
                shifting_prefix[start] -= 1
                shifting_prefix[end + 1] += 1
        
        char_list = list(s)
        ans = []

        running_sum = 0
        for i in range(n):
            running_sum += shifting_prefix[i]
            shift = (ord(char_list[i]) + (running_sum)%26) 
            if shift > 122:
                shift -= 26
            if shift < 97:
                shift += 26
            ans.append(chr(shift))
        return "".join(ans)
