# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0] * n

        for src, dest in edges:
            incoming[dest] += 1
        
        champions = [i for i, incoming_count in enumerate(incoming) if not incoming_count]

        if len(champions) > 1:
            return -1
        
        return champions[0]