# Problem: Sort The Students By Their Kth Score - https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key= lambda row: -row[k])
        # sort by specific column
        # sorted_matrix = sorted(matrix, key=lambda row: row[1])
        # sort by the sum of each row
        # sorted_matrix = sorted(matrix, key=lambda row: sum(row))
        # sort by first column on descending
        # sorted_matrix = sorted(matrix, key=lambda row: row[0], reverse=True)
        # sort by value on each row
        # sorted_matrix = sorted(matrix, key=lambda row: max(row))
        # sort by min value on each row
        # sorted_matrix = sorted(matrix, key=lambda row: min(row))
        # sort by the last element on each row
        # sorted_matrix = sorted(matrix, key=lambda row: row[-1])
        # sort by length of the row
        # /sorted_matrix = sorted(matrix, key=lambda row: len(row)) 


        """
        Sort by the Number of Odd Numbers in Each Row
        matrix = [[3, 2, 5], [1, 4, 6], [2, 1, 3]]
    sorted_matrix = sorted(matrix, key=lambda row: sum(1 for x in row if x % 2 != 0))
        print(sorted_matrix)
        Output: [[1, 4, 6], [2, 1, 3], [3, 2, 5]]
    Sort by the Absolute Difference Between the First and Last Element
        matrix = [[3, 2, 5], [1, 4, 6], [2, 1, 3]]
        sorted_matrix = sorted(matrix, key=lambda row: abs(row[0] - row[-1]))
        print(sorted_matrix)
        Output:
        [[1, 4, 6], [2, 1, 3], [3, 2, 5]]
        """