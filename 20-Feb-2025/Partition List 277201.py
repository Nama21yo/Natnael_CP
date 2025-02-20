# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_before = ListNode()
        dummy_after = ListNode()
        before_head = dummy_before
        after_head = dummy_after
        

        while head:
            # link it in before dummy
            if head.val < x:
                dummy_before.next = head
                dummy_before = dummy_before.next
            else: 
                dummy_after.next = head
                dummy_after = dummy_after.next
            head = head.next
        
        dummy_before.next = after_head.next
        # If you don't make this it will be affected
        dummy_after.next = None

        return before_head.next