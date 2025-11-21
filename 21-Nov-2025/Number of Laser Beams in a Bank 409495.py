# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        device_counts = [row.count('1') for row in bank if row.count('1') > 0]
        
        if len(device_counts) < 2:
            return 0
        
        beams = 0
        for i in range(1, len(device_counts)):
            # beams between consecutive non-empty rows = product of their device counts
            beams += device_counts[i - 1] * device_counts[i]
        
        return beams
