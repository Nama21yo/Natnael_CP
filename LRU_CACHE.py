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

        node =  self.node_map[key]
        temp = node.val
        self.put(key, node.val) # put  will implement it
        return temp

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            node = self.node_map[key]
            if node.next is None:
                node.val = value
            else:
                # add node before delete
                self.tail.next = Node(key, value)
                self.tail = self.tail.next
                self.node_map[self.tail.key] = self.tail

                next_node = node.next
                node.key = next_node.key
                node.val = next_node.val
                node.next = next_node.next

                self.node_map[next_node.key] = node
                
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