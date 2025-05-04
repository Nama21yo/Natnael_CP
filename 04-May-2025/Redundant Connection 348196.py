# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size
    def find(self, x):
        if x == self.root[x]:
            return x
        return self.find(self.root[x])
    
    def union(self,x,y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rootx] = rooty
                self.rank[rooty] += 1
            return True
        return False
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = UnionFind(len(edges) + 1) # to include the last edge
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]