# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        # Selection Sort
        for i in range(n):
            min_index =  i
            for j in range(i + 1, n):
                # will be descending
                if heights[j] > heights[min_index]:
                    min_index = j
            heights[i], heights[min_index] = heights[min_index], heights[i]
            names[i], names[min_index] = names[min_index], names[i]
        return names