# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #base case
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        # recursive case
        curr = list1
        if list1.val < list2.val:
            curr = list1
            curr.next = self.mergeTwoLists(list1.next,list2)
        else:
            curr = list2
            curr.next = self.mergeTwoLists(list1, list2.next)
        return curr







