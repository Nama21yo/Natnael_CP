# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats, students):
        max_position = max(max(seats), max(students))
        place = [0] * (max_position)
        n = len(seats)
        for i in range(n):
            place[seats[i] - 1] += 1
            place[students[i] - 1] -= 1
        moves = 0
        unmatched = 0
        for i in place:
            moves += abs(unmatched)
            unmatched += i
        return moves