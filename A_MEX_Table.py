def mex_table(mex):
    # If I try to keep 1 in the same row as 0,the max ans is : m(col) + 1
    # If I try to keep 1 in the sam col as 0, the max ans is : n(row) + 1
    # So my maximum ans is max(m + 1, n + 1) = max(n,m) + 1
    n = max(mex[0], mex[1])
    return n + 1

def main():
    t = int(input())  
    while t:
        mex = list(map(int, input().split(" "))) 
        print(mex_table(mex))
        t -= 1

main()

# For non-changing MEX - Counting sort / HashMap like Counter
# For Changing MEX - Use frequency hashmap + set Complement