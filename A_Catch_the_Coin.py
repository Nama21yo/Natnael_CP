def catch_the_coin(n, coins):
    for x, y in coins:
        # Check if Monocarp can reach before the coin falls
        if y < -1:
            print("NO")
        else:
            print("YES")

# Input
n = int(input())
coins = [tuple(map(int, input().split())) for _ in range(n)]

# Output result
catch_the_coin(n, coins)
