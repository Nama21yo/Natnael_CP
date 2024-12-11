def LOL(string, n):
    countl =  string.count("L")
    countO = string.count("O")

    ans = -1
    x = 0
    y = 0

    for cut in range(n - 1):
        if string[cut] == "L":
           x += 1
        elif string[cut] == "O":
           y += 1

        if (x != countl - x) and (y != countO - y):
            ans = cut + 1
            break
    return ans

    

def main():
    n = int(input())  # Read the value of n
    string = input()
    print(LOL(string, n))

main()