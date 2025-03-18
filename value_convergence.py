# Value Convergence
def can_find_pair(t, test_cases):
    results = []

    for n, a, v in test_cases:
        if n == 1:
            results.append("YES" if v[0] == a else "NO")
            continue

        v.sort()  # Sorting the list
        i, j = 0, 1  # Two pointers

        found = False
        while j < n and i < n:
            if v[i] + abs(a) == v[j]:
                found = True
                break
            elif v[i] + abs(a) < v[j]:
                i += 1
            else:
                j += 1

        results.append("YES" if found else "NO")

    return results

t = int(input())
test_cases = []
for _ in range(t):
    n, a = map(int, input().split())
    v = list(map(int, input().split()))
    test_cases.append((n, a, v))

# Process and print results
for result in can_find_pair(t, test_cases):
    print(result)


# Lecture Sleep
def max_awake_sum(n, k, a, t):
    overall = 0
    pr = [0] * n  # Prefix sum for sleeping moments

    # Compute prefix sum and overall awake sum
    for i in range(n):
        if i > 0:
            pr[i] = pr[i - 1]
        if t[i] == 0:
            pr[i] += a[i]
        else:
            overall += a[i]

    # Find the maximum additional sum we can gain by waking up for k minutes
    max_add = 0
    for i in range(k - 1, n):
        current_add = pr[i] - (pr[i - k] if i >= k else 0)
        max_add = max(max_add, current_add)

    return overall + max_add


# Input handling
n, k = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))

# Compute and print the result
print(max_awake_sum(n, k, a, t))

# Backspace
def backspaceCompare(self, s: str, t: str) -> bool:
        def valid_index(s: str, index: int) -> int:
            backspace_count = 0
            while index >= 0:
                if s[index] == '#':
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -= 1
                else:
                    break
                index -= 1
            return index

        s1 = len(s) - 1
        t1 = len(t) - 1

        while s1 >= 0 or t1 >= 0:
            s1 = valid_index(s, s1)
            t1 = valid_index(t, t1)

            if s1 >= 0 and t1 >= 0 and s[s1] != t[t1]:
                return False
            if (s1 >= 0) != (t1 >= 0):
                return False

            s1 -= 1
            t1 -= 1
        return True


# https://codeforces.com/contest/1676/problem/F
t = int(input())
for _ in range(t):
    n, k =  map(int, input().split())
    nums = sorted(map(int, input().split()))
    ans = [-1,-1]
    l = 0
    pre = -1
    cur_count = 0
    for r in range(n):
        if nums[r] == pre:
            cur_count += 1
        elif nums[r] > pre + 1:
            cur_count = 1
            l = r
        elif nums[r] == pre + 1:
            if cur_count < k:
                l = r
            cur_count = 1

        pre = nums[r]
        if cur_count >= k:
            if nums[r] - nums[l] >= ans[1] - ans[0]:
                ans[0] = nums[l]
                ans[1] = nums[r]

    if ans[0] == -1:
        print(-1)
    else:
        print(*ans)
# counting orders
mod = 10**9 + 7
t = int(input())
for _ in range(t):
    n = int(input())
    a =  sorted(map(int, input().split()))
    b =  sorted(map(int, input().split()))
    ans = 1
    l = 0
    for i in range(n):
        while l < n and a[i] > b[l]:
            l += 1
        if i == l:
            ans = 0
            break
        ans *= (l - i)
        ans %= mod
    print(ans % mod)
