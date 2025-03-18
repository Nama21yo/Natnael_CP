from collections import defaultdict
class ListNode:
    def __init__(self , data=0, next_node=None):
        self.data = data
        self.next = next_node

def search_list(l, key):
    while l and l.next != key:
        l = l.next
    return l # If key was not present in the List, L will have become null

def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node

def delete_after(node):
    node.next = node.next.next
def merge_two_sorted_lists(l1,l2):
    # Creates a placeholder for the result
    dummy_head = tail = ListNode()
    while l1 and l2:
        if l1.data < l2.data:
            tail.next , l1 = l1, l1.next
        else :
            tail.next , l2 = l2 , l2.next
        tail = tail.next
    # Appends the remaining nodes of Ll or L2
    tail.next = l1 or l2
    return dummy_head.next
# def rverse_list

class Node:
    def __init__(self,num , ugly):
        self.num = num
        self.ugly = ugly
        self.prev = None
        self.next = None



for _ in range(int(input())):
    N , u = map(int, input().split())
    head = Node(1,u)
    nei = list(map(int, input().split()))
    ugly = list(map(int, input().split()))


    monster = {}
    monster[1] = head
    next_number = 2
    count = 1
    ans = []

    def merge(left , right):
        global count
        newNode = Node(min(left.num , right.num) , left.ugly + right.ugly)
        del monster[left.num]
        del monster[right.num]
        
        monster[newNode.num] = newNode

        if count == 2:
           pass
        else:        
            newNode.next = right.next
            right.next.prev = newNode

            newNode.prev = left.prev
            left.prev.next = newNode

        count -= 1
        return newNode
    

    for i in range(N):
        nei_ind = nei[i]
        neighbour = monster[nei_ind]
        currentMonster = Node(next_number , ugly[i])
        monster[next_number] = currentMonster
        next_number += 1
        count += 1

        if neighbour.next == None:
            neighbour.next = neighbour.prev = currentMonster
            currentMonster.next = currentMonster.prev = neighbour
  

        else:

            currentMonster.next = neighbour.next
            currentMonster.prev = neighbour
            neighbour.next.prev = currentMonster
            neighbour.next = currentMonster
        
        curr = currentMonster

        while curr.next != None and curr.prev != None and (curr.ugly == curr.prev.ugly or curr.ugly == curr.next.ugly):
            
            if curr.ugly == curr.prev.ugly:
                curr = merge(curr.prev , curr)
            else:
                curr = merge(curr , curr.next)
        
            
        ans.append(count)

    print(*ans)
# def has-cycle (head) :
# fast=slow=head
# while fast and fast. next and fast. next. next:
# slow, fast = slow.next, fast.next.next
# if slow is fast: # There is a cyc7e.
# # Tries to find the start of the cyc7e.
# slow = head
# # Both pointers advance at the sane time,
# rhile slow is not fast:
# slow , fast = sIow. next , fast . next
# return slow # sTow is the start of cycle
# return None # No cyc7e.

# def has-cycIe (head) :
# def cycle-len(end):
# start , step = end, 0
# rhile True:
# step += 1
# start = start.next
# if start is end
# return step
# M 11 7 5 3 2 X
# 86
# fast=slow=head
# rhile fast and fast. next and fast. next, next:
# slow, fast = slow.next, fast.next.next
# if slow is fast:
# # Finds the start of the cycle.
# cycle_Ien_advanced_iter = head
# for 
# - 
# in range(cycIe-len(slow)):
# cycle_len_advanced_iter = cycle_Ien_advanced_iter. next
# it = head
# # Both iterators advance in tandem.
# rhile it is not cycle_Len_advanced_iter:
# it = it, next
# cycle_1en_advanced_iter = cycle_Ien_advanced_iter. next
# return it # iter is the start of cycle.
# return None # No cycle.

# def overlapping-no-cycIe-lists(L1, L2)
# def length(L):
# length = 0
# while L:
# length += 1
# L = L. next
# return length
# L1_Ien, L2_Ien = length(L1), length(L2)
# if Ll-Ien > L2-Ien:
# Ll, LZ = L2, LL # L2 is t}le longer list
# # Advances the Tonger ljst to get equaT length lists
# for 
# - 
# in range(abs(Ll-len - L2-Ien)):
# L2 = L2. next
# nhile Ll and L2 and Ll is not L2:
# Ll, L2 = Ll.next, L2.next
# return Ll # None implies there is no overTap between Ll and L