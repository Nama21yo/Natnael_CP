import sys

def iinp():
    return int(sys.stdin.readline().strip())

def linp():
    return list(map(int, sys.stdin.readline().strip().split()))

def countMaxBallons(assistants, time):
    max_balloon = 0
    assistant_balloon = []
    
    for t, z, y in assistants:
        full_cycles = time // (t * z + y)
        balloon_inflated = full_cycles * z
        remaining_time = time % (t * z + y)
        if remaining_time >= (t * z):
            balloon_inflated += z
        else:
            balloon_inflated += remaining_time // t
        max_balloon += balloon_inflated
        assistant_balloon.append(balloon_inflated)

    return max_balloon, assistant_balloon

def solve(assistants, n, m):
    l, r = -1, int(2e9) + 1  # Updated to match C++ range
    while r > l + 1:
        mid = (l + r) // 2
        max_balloon, _ = countMaxBallons(assistants, mid)
        if max_balloon >= m:
            r = mid
        else:
            l = mid
    # Compute the final distribution of balloons
    final_balloons = []
    remaining_m = m
    for t, z, y in assistants:
        balloons = countMaxBallons([(t, z, y)], r)[0]
        allocated = min(remaining_m, balloons)
        final_balloons.append(allocated)
        remaining_m -= allocated
    return r, final_balloons

def main():
    m, n = linp()
    assistants = [linp() for _ in range(n)]
    time, balloon_per_assistant = solve(assistants, n, m)
    print(time)
    print(*balloon_per_assistant)

if __name__ == '__main__':
    main()
