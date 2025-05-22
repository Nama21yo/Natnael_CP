# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        
        for i,node in enumerate(lists):
            if node:
                heappush(minHeap, (node.val, i, node))
        
        dummy = ListNode()
        current = dummy

        while minHeap:
            val,i,node = heappop(minHeap)
            current.next = node
            current = current.next

            if node.next:
                heappush(minHeap, (node.next.val, i, node.next))
        return dummy.next