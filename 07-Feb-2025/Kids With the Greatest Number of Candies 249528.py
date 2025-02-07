# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = 0

        for candy in candies:
            maxi = max(maxi, candy)
        
        ans = []
        for candy in candies:
            if candy + extraCandies >= maxi:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans