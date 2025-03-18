# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        maxi = max(arr1)

        count_arr = [0]*(maxi + 1)

        for num in arr1:
            count_arr[num] += 1
        output = []

        for i in range(len(arr2)):
            while count_arr[arr2[i]] > 0:
                output.append(arr2[i])
                count_arr[arr2[i]] -= 1
        
        for i in range(maxi + 1):
            while count_arr[i] > 0:
                output.append(i)
                count_arr[i] -= 1
        
        return output