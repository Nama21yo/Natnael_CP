# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.findSum(n)
        
        while fast != 1 and fast != slow:
            slow = self.findSum(slow)
            fast = self.findSum(self.findSum(fast))
        
        return fast == 1
    def findSum(self,n):
        sum = 0
        while n > 0:
            sum += (n % 10) * (n % 10)
            n = n//10
        return sum
        