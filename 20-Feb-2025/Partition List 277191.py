# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_before = ListNode(0)
        dummy_after = ListNode(0)
        before_head = dummy_before
        after_head = dummy_after
        curr = head
        
        while curr:
            # link it in before dummy
            if curr.val < x:
                dummy_before.next = ListNode(curr.val)
                dummy_before = dummy_before.next
            else: 
                dummy_after.next = ListNode(curr.val)
                dummy_after = dummy_after.next
            curr = curr.next
        
        dummy_before.next = after_head.next

        return before_head.next