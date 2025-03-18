# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        n = len(arr)
        ans = [0]*n
        ans[-1] = -1
        ans[-2] =  arr[-1]
        maxi = ans[-2]
        for i in range(n - 3,-1,-1):
            maxi = max(arr[i + 1], maxi)
            ans[i] = maxi
        return ans


        