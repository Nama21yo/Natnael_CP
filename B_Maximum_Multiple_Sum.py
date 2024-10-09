def maximium_multiple_sum(n):
   if(n == 3):
        return 3
   return 2

def main():
    t = int(input())  # Read the value of n
    for _ in range(t):
        n = int(input())
        print(maximium_multiple_sum(n))

main()