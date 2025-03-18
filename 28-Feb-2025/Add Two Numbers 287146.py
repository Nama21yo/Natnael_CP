# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            temp =  curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reversed_1 = self.reverse(l1)
        # reversed_2 = self.reverse(l2)
        # print(reversed_1)
        # print(reversed_2)
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:  # can be more than both l1 and l2 eg. 999 and 9
        
            sumi = l1.val if l1 else 0
            sumi += l2.val if l2 else  0 
            sumi += carry

            carry = sumi // 10 
            sumi = sumi % 10
            curr.next = ListNode(sumi)

            
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        print(curr)
        return dummy.next