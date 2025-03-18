# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

# Implementing using Singly Linked list
class Node:
    def __init__(self, key=0, val = 0, next=None):
        self.key = key
        self.val = val
        self.next = next
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = self.head
        self.node_map = {}

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1

        node = self.node_map[key]
        
        if node != self.tail:
            prev = self.head
            while prev.next and prev.next != node:
                prev = prev.next
            prev.next = node.next  
            self.tail.next = node 
            self.tail = node
            node.next = None
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value  
            # Move node to the end (most recently used)
            if node != self.tail:
                prev = self.head
                while prev.next and prev.next != node:
                    prev = prev.next
                prev.next = node.next  
                self.tail.next = node  
                self.tail = node
                node.next = None
        
        else:
            new_node = Node(key, value)
            self.tail.next = new_node
            self.tail = new_node
            self.node_map[key] = new_node

            
            if len(self.node_map) > self.capacity:
                least_used = self.head.next
                del self.node_map[least_used.key]  
                self.head.next = least_used.next  

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)