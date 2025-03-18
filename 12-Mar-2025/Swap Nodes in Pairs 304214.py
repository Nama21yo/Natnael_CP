# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def size_ll(self, head):
        """
         # Base Case
        if head is None:
        return 0
        # Count this node plus the rest of the list
        return 1 + count_nodes(head.next)
        """
        size = 0
        while head: # sincle it is local variableno problem if curr or head
            head = head.next
            size += 1
        return size
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        #  4 >> 5, k = 3
        if self.size_ll(head) < 2:
            return head
        # recursive case
        # do the reverse for the first part and let
        # recursion do the rest for  you
        prev = None
        curr = head
        count  = 0
        while count < 2:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1
        
        if curr:
            head.next = self.swapPairs(curr)
        
        return prev
