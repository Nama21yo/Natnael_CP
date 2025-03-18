# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        num_boats = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                num_boats += 1
                l += 1
                r -= 1
            else:
                num_boats += 1
                # it is heavier
                r -= 1
        return num_boats
                