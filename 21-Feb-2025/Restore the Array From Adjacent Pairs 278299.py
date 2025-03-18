# Problem: Restore the Array From Adjacent Pairs - https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        pairs = defaultdict(list)
        n = len(adjacentPairs)
        for pair in adjacentPairs:
            pairs[pair[0]].append(pair[1])
            pairs[pair[1]].append(pair[0])
        # pairs >> {2: [1, 3], 1: [2], 3: [4, 2], 4: [3]})

        # find your start
        start = - (10 ** 5 + 1)
        for key,value in pairs.items():
            if len(value) == 1:
                start = key
                break
        # iterate and starting implemnting your result array
        # left << el >> right so left and right are adj to el
        ans = [start]
        left = -(10 ** 5 + 1)
        for i in range(1, n + 1):
            val = pairs[start]
            next_el = val[0] if val[0] != left else val[1]
            ans.append(next_el)
            left = start
            start = next_el
        return ans