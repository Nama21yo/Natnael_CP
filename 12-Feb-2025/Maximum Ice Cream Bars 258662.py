# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxi = 0
        # Find my maximum
        for cost in costs:
            maxi = max(maxi, cost)
        
        # make a count_arr for counting sort
        count_arr = [0] * (maxi + 1)
        for cost in costs:
            count_arr[cost] += 1
        
        # iterate and decrement your arr
        ans = 0
        for i in range(1, maxi + 1):
            while count_arr[i] > 0:
                if i <= coins:
                    ans += 1
                    count_arr[i] -= 1
                    coins -= i
                else:
                    break
        return ans
                
            


