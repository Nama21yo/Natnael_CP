# Problem: Freedom Trail - https://leetcode.com/problems/freedom-trail/

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def dfs(ring, index):
            if index == len(key):
                return 0

            ans = float("inf")

            # For each ring[i] == key[index], we rotate the ring to match the ring[i]
            # with the key[index], then recursively match the newRing with the
            # key[index + 1..n).
            for i, r in enumerate(ring):
                if r == key[index]:
                    minRotates = min(i, len(ring) - i)
                    newRing = ring[i:] + ring[:i]
                    remainingRotates = dfs(newRing, index + 1)
                    ans = min(ans, minRotates + remainingRotates)

            return ans

        return dfs(ring, 0) + len(key)