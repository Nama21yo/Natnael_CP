# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph = {i: [] for i in range(len(matrix))}
        graph = defaultdict(list)
        # convert to graph
        for row, col in prerequisites:
            graph[col].append(row)
        white = 0
        grey = 1
        black = 2
        color = [white] * numCourses 

        def dfs(node):
            color[node] = grey
            result = True
            for neigh in graph[node]:
                if color[neigh] == grey:
                    return False
                elif color[neigh] == white:
                    result = result and dfs(neigh)
            # backtrack
            color[node] = black
            return result
        ans = True
        for node in range(numCourses):
            if color[node] == white:
                ans = ans and dfs(node)
        return ans