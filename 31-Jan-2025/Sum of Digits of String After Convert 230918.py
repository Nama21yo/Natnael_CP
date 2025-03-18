# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def get_sum(self, num):
        sumi = 0
        while num > 0:
            sumi += (num % 10)
            num //= 10
        return sumi
    
    def getLucky(self, s: str, k: int) -> int:
        string = ""
        for char in s:
            string += str((ord(char) - ord('a')) + 1)
        
        sumi = 0
        for char in string:
            sumi += int(char)
        

        if k == 1:
            return sumi
        
        transform = sumi
        while k > 1:
            transform = self.get_sum(sumi)
            sumi = transform
            k -= 1

        return sumi