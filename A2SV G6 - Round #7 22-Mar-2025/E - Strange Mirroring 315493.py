# Problem: E - Strange Mirroring - https://codeforces.com/gym/596141/problem/E


from math import ceil, log2
 
t = int(input())
 
for _ in range(t):
    s = input()
    n = len(s)
    q = int(input())
    queries = list(map(int, input().split()))
    
    def find(k):
        if 1 <= k <= n:
            return s[k - 1]
        
        curr_level = ceil(log2(ceil(k / n)))
        k = k - 2 ** (curr_level - 1) * n
 
        return find(k).swapcase()
    
    ans = []
    for k in queries:
        ans.append(find(k))
 
    print(*ans)
