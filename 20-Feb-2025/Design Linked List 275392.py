# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next
class MyLinkedList:
    def __init__(self):
        self.dummy = Node()
        self.tail= None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr_idx = 0
        curr_node = self.dummy.next # remember this one that should be head

        while curr_idx < index:
            curr_node = curr_node.next
            curr_idx += 1

        # we need the value at the index
        return curr_node.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        head = self.dummy.next
        new_node.next = head
        self.dummy.next = new_node

        # if tail and head  point to the same
        if not self.tail:
            self.tail = new_node
        
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        self.size += 1
        if not self.tail:
            self.dummy.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size: # but not equal
            return
        
        if index == self.size:
            self.addAtTail(val)
        else:
            # for the rest index starting 0 >> size - 1
            curr_idx = 0
            curr_node = self.dummy

            while curr_idx < index:
                curr_node = curr_node.next
                curr_idx += 1
            
            new_node = Node(val)
            new_node.next = curr_node.next
            curr_node.next = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        curr_idx = 0
        curr_node = self.dummy
        while curr_idx < index:
            curr_node = curr_node.next
            curr_idx += 1
        
        # for the tail
        curr_node.next = curr_node.next.next
        if not curr_node.next:
            self.tail = curr_node
            # self.tail = curr_node.next >> This was the error
        self.size -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)