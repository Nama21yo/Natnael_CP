# Problem: E - Weird and Ugly Monsters - https://codeforces.com/gym/590053/problem/E

from collections import defaultdict
#use double ll
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
