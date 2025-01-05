def base_conversion(n):
    if n == 0:
        return ""
    return base_conversion(n // 2) + str(n % 2) 
    # return base_conversion(n//2, decimal * 10)  + (n % 2)
    # decimal = decimal * 10 + (n % 2)

def main():
    t = int(input())
    while t:
        n = int(input())  
        print(base_conversion(n))
        t -= 1

main()