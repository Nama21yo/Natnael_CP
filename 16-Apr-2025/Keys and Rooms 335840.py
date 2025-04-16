# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)
        dfs(0)
        # check all rooms are visited
        return len(visited) == len(rooms)