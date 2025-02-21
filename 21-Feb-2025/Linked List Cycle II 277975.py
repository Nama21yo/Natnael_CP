# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def check_cycle(head):
            # the slow and fast pointer must meet

            slow = head
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return [True, fast]
            return [False, fast]
        

        cycle_exist, fast = check_cycle(head)
        if not cycle_exist: return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            # pos += 1
        return slow
        