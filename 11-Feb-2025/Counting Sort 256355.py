# Problem: Counting Sort - https://www.hackerrank.com/challenges/countingsort1/problem

def countingSort(arr):
    # Write your code here
    count = [0]*100
    for num in arr:
        count[num]+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
