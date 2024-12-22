def prepare_olmpiad(mono, streo, n):  
    ans = 0

    for i in range(n - 1):
        if mono[i] > streo[i + 1]:
            ans += mono[i] - streo[i + 1]
    ans += mono[n - 1]

    return ans  

def main():  
    t = int(input())   
    while t:  
        n = int(input())  
        mono = list(map(int, input().split()))  
        streo = list(map(int, input().split()))  
        print(prepare_olmpiad(mono, streo, n))  
        t -= 1  

if __name__ == "__main__":  
    main()