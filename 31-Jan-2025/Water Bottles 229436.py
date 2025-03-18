# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
       total_drinks = numBottles

       while numBottles >= numExchange:
            rem = numBottles % numExchange
            numBottles = numBottles // numExchange
            total_drinks += numBottles
            numBottles += rem
        
       return total_drinks


        