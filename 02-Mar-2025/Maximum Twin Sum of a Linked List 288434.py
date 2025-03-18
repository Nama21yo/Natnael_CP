# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # first find the middle element
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # print(slow)
        # now slow is my middle so reverse froom that one
        dummy = ListNode(0)
        dummy.next = slow.next

        prev = None
        curr = dummy
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # prev id the reversed one
        # print(prev)
        max_sum = 0
        tail = head
        while prev.next:
            # print(tail.val, prev.val)
            max_sum = max(tail.val + prev.val, max_sum)
            prev = prev.next
            tail = tail.next
        return max_sum
        