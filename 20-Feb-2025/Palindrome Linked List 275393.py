# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool: 
    #   Find the middle
        slow, fast = head, head
        while fast and fast.next: # for both even and odd
            slow = slow.next
            fast = fast.next.next
    #   Reverse the second part
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # Compare first and second half
        first, second = head, prev
        while second:  # Only check the second half
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True
