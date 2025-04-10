# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adj_list = {emp.id :emp for emp in employees}
        def dfs(id):
            result = adj_list[id].importance
            for neigh in adj_list[id].subordinates:
                result += dfs(neigh)
            return result
        return dfs(id)



            