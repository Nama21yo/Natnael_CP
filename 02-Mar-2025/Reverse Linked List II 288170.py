# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        left_side = dummy

        for _ in range(1, left):
            left_side = left_side.next
        # left_side will be the last left side

        prev = None
        curr = left_side.next
        last_node = curr # the 1st el will be the last in reverse
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev =  curr
            curr = temp
        
        # connect it with the left side
        left_side.next = prev
        # connect it with the right side
        last_node.next = curr # the last unreversed part wil be curr 

        return dummy.next
