# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value_count = 0    
        self.value = value
        self.k = k 

    def consec(self, num: int) -> bool:
        # self.queue.append(num)
        if len(self.queue) >= self.k:
            val = self.queue.popleft()
            if val == self.value:
                self.value_count -= 1
        self.queue.append(num)
        if num == self.value:
            self.value_count += 1
        return self.k == self.value_count
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)