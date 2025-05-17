# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * n
        prefix[0] = arr[0]

        for i in range(1,n):
            prefix[i] = prefix[i - 1] ^ arr[i]
        
        ans = []
        #  if l is not zero 
        #     XOR = prefix[r] ^ prefix[l-1]
        # else 
        #     XOR = prefix[r].
        for l, r in queries:
            xor = 0
            if l != 0:
                xor = prefix[r] ^ prefix[l - 1]
            else:
                xor = prefix[r]
            ans.append(xor)
        return ans 