# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(instructions)
        counts = [0] * (max_val + 2)
        
        def update(index, delta):
            while index < len(counts):
                counts[index] += delta
                index += index & -index
        
        def query(index):
            result = 0
            while index > 0:
                result += counts[index]
                index -= index & -index
            return result

        cost = 0
        for i, num in enumerate(instructions):
            left = query(num - 1)
            right = i - query(num)
            cost += min(left, right)
            update(num, 1)

        return cost % MOD
