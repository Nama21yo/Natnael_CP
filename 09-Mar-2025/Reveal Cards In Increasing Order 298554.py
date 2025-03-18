# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

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
        