# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        # remember this thing
        curr = list1
        if list1.val < list2.val:
            curr = list1
            curr.next = self.merge(list1.next, list2)
        else:
            curr = list2
            curr.next = self.merge(list1, list2.next)
        return curr

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeSort(head):
            if head is None or head.next is None:
                return head
            mid = self.getMid(head)
            left = head
            right = mid.next
            # break them apart
            mid.next = None
            left = mergeSort(left)
            right = mergeSort(right)
            return self.merge(left, right)
        return mergeSort(head)


