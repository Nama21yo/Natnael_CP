# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        prereq_sets = [set() for _ in range(numCourses)]

        for pre, course in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        while queue:
            course = queue.popleft()
            for neighbor in graph[course]:
                # Add current course and its prerequisites to the neighbor's set
                prereq_sets[neighbor].update(prereq_sets[course])
                prereq_sets[neighbor].add(course)
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return [u in prereq_sets[v] for u, v in queries]
