# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n):
            mini = i
            for j in range(i, n):
                if arr[j] < arr[mini]:
                    mini = j
            arr[i], arr[mini] = arr[mini], arr[i]