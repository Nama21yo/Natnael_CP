# Problem: Insertion Sort List - https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self,head):
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    def merge(self,list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        curr = list1
        if list1.val < list2.val:
            curr = list1
            curr.next = self.merge(list1.next, list2)
        else:
            curr = list2
            curr.next = self.merge(list1, list2.next)
        return curr

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # using merge sort
        def mergesort(head):
            """
            # find mid
            # recursively sort 2 parts
            # merge them
            """
            if head is None or head.next is None:
                return head
            
            mid = self.getMid(head)
            left = head
            right = mid.next
            # break them apart
            mid.next = None

            left = mergesort(left)
            right = mergesort(right)

            return self.merge(left,right)
        return mergesort(head)
