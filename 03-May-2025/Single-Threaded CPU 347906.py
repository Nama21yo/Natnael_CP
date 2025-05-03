# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap  = []
        for idx, task in enumerate(tasks):
            task.append(idx)
        tasks.sort()
        result , minHeap = [],[]
        curr_task = 0
        curr_time = 0
        while minHeap or curr_task < len(tasks):
            while curr_task < len(tasks) and curr_time >= tasks[curr_task][0]:
                heappush(minHeap, [tasks[curr_task][1], tasks[curr_task][2]])
                curr_task += 1
            if minHeap:
                processTime, task = heappop(minHeap)
                curr_time += processTime
                result.append(task)
            else:
                curr_time = tasks[curr_task][0]
        return result