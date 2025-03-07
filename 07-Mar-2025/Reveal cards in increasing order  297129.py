# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

from collections import deque
# q = deque()
# q.append('a') >> enqueue >> Insert in the last
# print(q.popleft()) >> dequeue >> Remove from the first


class Solution:  
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:    
        deck.sort()
        n = len(deck)
        queue = deque(range(n)) # for keeping the indexes

        ans = [0] * n

        for card in deck:
            ans[queue.popleft()] = card
            # if my queue isn't empty
            if queue:
                queue.append(queue.popleft())
        return ans
        