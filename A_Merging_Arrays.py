def merging_arrays(arr1, n1, arr2, n2):
    l = 0
    h = 0

    merge = [0]* (n1 + n2)

    k = 0
    while l < n1 and h < n2:
        if arr1[l] < arr2[h]:
            merge[k] = arr1[l]
            l += 1
        else:
            merge[k] = arr2[h]
            h += 1
        k += 1
    
    while l  < n1:
        merge[k] = arr1[l]
        l += 1
        k += 1
    
    while h < n2:
        merge[k] = arr2[h]
        h += 1
        k += 1
    return merge
    



def main():
    n1, n2 = map(int, input().split()) 
    arr1 = list(map(int, input().split()))  
    arr2 = list(map(int, input().split()))  
    print(" ".join(map(str, merging_arrays(arr1, n1, arr2, n2))))

main()