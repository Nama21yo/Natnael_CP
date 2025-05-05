# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size
    
    def find(self, x):
        if x != self.root[x]:  # Path compression
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1
            return True
        return False

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        mapMail = {}
        dsu = UnionFind(n)

        for i in range(n):
            for mail in accounts[i][1:]:  # Start from index 1 to skip account name
                if mail not in mapMail:
                    mapMail[mail] = i
                else: 
                    dsu.union(i, mapMail[mail])
        
        mergedMail = [[] for _ in range(n)] 
        for key, val in mapMail.items():
            parent = dsu.find(val)
            mergedMail[parent].append(key)
        
        ans = []
        for i in range(n):
            if not mergedMail[i]: continue
            mergedMail[i].sort()
            temp = [accounts[i][0]] + mergedMail[i]
            ans.append(temp)
            
        return ans
