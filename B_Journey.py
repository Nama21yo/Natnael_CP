def journey(arr):  
    n = arr[0] 
    d =  arr[1] + arr[2] + arr[3]

    days = (n//d)
    n = n - (d * (days))
    days *= 3

    if n > arr[1] + arr[2]:
        days += 3
    elif n > arr[1]:
        days += 2
    elif n > 0:
        days += 1
    
    return days  

def main():  
    t = int(input())  
    while t > 0:  
        arr = list(map(int, input().split()))  
        print(journey(arr))  
        t -= 1  

main()