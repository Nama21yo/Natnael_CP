# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count_arr = Counter(arr)
        freq_sorted = sorted(count_arr.items(), key = lambda num: -num[1])
        # The optimized one is using counting sort of (n + 1)
        sumi = 0
        n = len(arr)
        count_set = 0
        i = 0
        while sumi < n // 2:
            sumi += freq_sorted[i][1]
            count_set += 1
            i += 1
            if i == n:
                break
        return count_set
