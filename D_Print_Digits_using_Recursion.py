def print_d(n):  
    if n == 0:  
        return  
    print_d(n // 10)  
    print(n % 10, end=" ")  

def main():  
    t = int(input())  
    while t:  
        n = int(input())  
        if n == 0:   
            print(0)  
        else:  
            print_d(n)  
        print()  
        t -= 1  

main()