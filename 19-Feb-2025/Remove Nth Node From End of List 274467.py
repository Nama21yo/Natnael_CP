# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        print(length)
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        idx_del = length - n
        i = 0
        while i < idx_del:
            curr = curr.next
            i +=  1
        curr.next = curr.next.next
        return dummy.next