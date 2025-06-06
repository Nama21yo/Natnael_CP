# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        parent = [i for i in range(len(strs))]
        rank = [0] * len(strs)

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            root_a, root_b = find(a), find(b)
            if root_a != root_b:
                if rank[root_a] > rank[root_b]:
                    parent[root_b] = root_a
                elif rank[root_b] > rank[root_a]:
                    parent[root_a] = root_b
                else:
                    parent[root_b] = root_a
                    rank[root_a] += 1

        def is_similar(x: str, y: str):
            diff_cnt = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    # important! False when diff_cnt > 2
                    # assigns the result of diff_cnt + 1 back to diff_cnt and returns the new value of diff_cnt
                    if (diff_cnt := diff_cnt + 1) > 2:
                        return False
            return True

        group_cnt = len(strs)
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                # important! check whether they are in the same group first.
                if find(i) != find(j) and is_similar(strs[i], strs[j]):
                    group_cnt -= 1
                    union(i, j)
        return group_cnt