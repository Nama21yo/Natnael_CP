# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy
        current = head
        while current:
            if current.val != val:
                prev.next = ListNode(current.val)
                prev = prev.next

            current = current.next
        return dummy.next
                