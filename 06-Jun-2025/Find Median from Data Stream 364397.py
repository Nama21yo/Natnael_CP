# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:
    def __init__(self):
        self.lo = []  
        self.hi = []  

    def addNum(self, num):
        heappush(self.lo, -num)             
        heappush(self.hi, -self.lo[0])      
        heappop(self.lo)
        
        if len(self.lo) < len(self.hi):
            heappush(self.lo, -self.hi[0])
            heappop(self.hi)
            
    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]                  
        else:
            return (self.hi[0] - self.lo[0]) / 2  