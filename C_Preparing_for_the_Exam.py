from functools import reduce

def prepare_exam(nmk, am, qk):
    n, m ,k = nmk

    if n == k:
        return "1"*(m)
    
    if k <= n - 2:
        return "0"*(m)
    
    # Find the missing one using sum(n (n +1) /2) or using xor
    # using XOR
    # # Using reduce() + lambda + "^" operator
    # res = reduce(lambda x, y: x ^ y, test_list)
    tot = reduce(lambda x, y: x ^ y, am)
    know = reduce(lambda x, y: x ^ y, qk)
    true_ans = tot ^ know 
    ans = ""
    for a in am:
        if a == true_ans:
            ans += "1"
        else:
            ans += "0"
    return ans
def main():
    t = int(input()) 
    while t:
        nmk = list(map(int, input().split())) 
        am = list(map(int, input().split()))
        qk = list(map(int, input().split()))
        print(prepare_exam(nmk, am, qk))
        t -= 1

main()