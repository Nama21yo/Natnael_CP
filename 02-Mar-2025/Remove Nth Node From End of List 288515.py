# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        # to delete you should go  one step further
        # take fast n steps ahead
        for _ in range(n + 1):
            if fast:
                fast = fast.next
        # move fast and slow equally until become null
        while fast: # move size - n steps
            slow = slow.next
            fast = fast.next
        
        #slow is my n + 1 node
        slow.next = slow.next.next
        return dummy.next