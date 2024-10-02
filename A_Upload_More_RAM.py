def upload_more_ram():
    t = int(input()) 
    for _ in range(t):
        n, k = map(int, input().split())
        if k == 1:
            print(n)
        else:
                # 5 1
                # 1 1 1 1 1 = 5

                # 2 2
                # 10 1 = (n - 1) * k + 1 = 3

                # 2 3
                # 100 1 = (n - 1) * k + 1 = 4

                # 1 7
                # 1 = (n - 1) * k + 1 = 1
            print((n - 1) * k + 1)

upload_more_ram()
