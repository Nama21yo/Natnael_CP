# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/

import random
class RandomizedSet:
    def __init__(self):
        self.my_map = defaultdict(int)
        self.my_list = []
    def insert(self, val: int) -> bool:
        if val not in self.my_map:
            self.my_map[val] = len(self.my_list)
            self.my_list.append(val) 
            return True
        return False 

    def remove(self, val: int) -> bool:
        if val in self.my_map:   
            rem_index = self.my_map[val]
            # Don't forget it!!!
            self.my_map[self.my_list[-1]] = rem_index
            self.my_list[rem_index], self.my_list[-1] = self.my_list[-1], self.my_list[rem_index]  
            self.my_list.pop()
            self.my_map.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        my_random = random.randint(0, len(self.my_list) - 1)
        return self.my_list[my_random]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()