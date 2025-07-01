# Problem: The Number of the Smallest Unoccupied Chair - https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/

class Solution:
    def smallestChair(self, times, targetFriend):
        n = len(times)
        events = []
        for i in range(n):
            arrivali, leavingi = times[i]
            events.append((arrivali, 1, i))  # 'arrive' event
            events.append((leavingi, 0, i)) 
        events.sort()
        available_chairs = list(range(n))
        heapq.heapify(available_chairs)
        occupied = []
        friend_to_chair = {}
        
        for time, event_type, friend in events:
            if event_type == 0:  # 'leave' event
                chair = friend_to_chair.pop(friend)
                heapq.heappush(available_chairs, chair)
            else: 
                chair = heapq.heappop(available_chairs)
                friend_to_chair[friend] = chair
                if friend == targetFriend:
                    return chair
        return -1