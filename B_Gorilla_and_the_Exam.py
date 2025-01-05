from collections import defaultdict  

def gorilla_exam(nums, n, k):  
    count_arr = defaultdict(int)  
    # Count the elements  
    for num in nums:  
        count_arr[num] += 1  
    
    # Approach - Be greedy
    # 1. pick a number with least frequency
    # 2. overide that number with the element that have the largest freq
    # 3. return the number of distinct elements

    # Create a list of frequencies sorted in increasing order  
    frequencies = sorted(count_arr.values())  
    
    # Reduce distinct elements using available k operations  
    distinct_count = len(frequencies)  # Initial distinct elements count  
    for freq in frequencies:  
        if k >= freq:  
            k -= freq  # We can eliminate this number completely  
            distinct_count -= 1  # One distinct element removed  
        else:  
            break  # No more operations can affect further numbers  
    
    return distinct_count if distinct_count != 0 else 1

def main():  
    t = int(input())   
    while t:  
        n, k = map(int, input().split(" "))  
        nums = list(map(int, input().split(" ")))  
        print(gorilla_exam(nums, n, k))  
        t -= 1  

if __name__ == "__main__":  
    main()