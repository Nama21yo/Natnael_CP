# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:  
        passenger_changes = [0] * 1001  
        
        for trip in trips:  
            passenger_changes[trip[1]] += trip[0]  
            passenger_changes[trip[2]] -= trip[0]  
        
        for change in passenger_changes:  
            capacity -= change  
            if capacity < 0:  
                return False  
        
        return True