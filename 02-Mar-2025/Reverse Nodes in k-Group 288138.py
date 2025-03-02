# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       # base case
        #  4 >> 5, k = 3
        if self.size_ll(head) < k:
            return head
        # recursive case
        # do the reverse for the first part and let
        # recursion do the rest for  you
        prev = None
        curr =  head
        count = 0
        while count < k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1
        # make a recursive call
        if curr: # curr isn't None
            head.next = self.reverseKGroup(curr, k)
        return prev