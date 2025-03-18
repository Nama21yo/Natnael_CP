# Problem: Insertion Sort List - https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0) 
        dummy.next = head
        curr = head.next
        prev = head

        while curr:
            nxt = curr.next  
            runner = dummy
            if curr.val < prev.val:
                while runner.next and runner.next.val < curr.val:
                    runner = runner.next
                prev.next = curr.next
                curr.next = runner.next
                runner.next = curr
            else:
                prev = curr  
            curr = nxt  

        return dummy.next