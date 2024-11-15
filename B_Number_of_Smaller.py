def number_of_smaller(arr1, n1, arr2, n2):
    l = 0
    h = 0

    smaller = [0]* (n2)

    k = 0
    while h < n2:
        while l < n1 and arr1[l] < arr2[h]: 
            l += 1
        smaller[k] = l
        k += 1
        h += 1
    
    return smaller
    



def main():
    n1, n2 = map(int, input().split()) 
    arr1 = list(map(int, input().split()))  
    arr2 = list(map(int, input().split()))  
    print(" ".join(map(str, number_of_smaller(arr1, n1, arr2, n2))))

main()