class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # 15 //4 = 3 15%4 = 3  3+3//4 = 1 2//4 =0
        # count = 15 + 3 + 1
        # 9 // 3 = 3 9 % 3 = 0  3 + 0 // 3 = 1 1 % 3 = 1 
        # count = 9 + 3 + 1
        total_drinks = numBottles
        while numBottles >= numExchange:
            # remainder
            rem = (numBottles % numExchange) # 3
            # floor it
            numBottles = numBottles // numExchange # 3
            total_drinks += numBottles
            numBottles += rem
        return total_drinks

        