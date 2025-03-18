from __future__ import division, print_function
import itertools
import sys
import os
import bisect
if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def solve(price,pay,n,m):
    # Create a multiset to store the prices of all tickets
    maxPrice = sorted(price)

    # Create an array answer to store the answer for each customer
    ans = [0 for j in range(len(pay))]

    # Now iterate through every customer
    for i in range(len(pay)):

        temp = pay[i]

        # Find the upper bound of maximum price offered by customer in the multiset
        itr = bisect.bisect(maxPrice,temp)

        # If it points to the beginning, that means no ticket is available for the customer
        # Otherwise, decrement the iterator and get the value out of it and then erase that value from the multiset
        if (itr == 0):
            ans[i] = -1
        else:
            itr -= 1
            ans[i] = maxPrice[itr]
            maxPrice.remove(ans[i])

    # Return the array answer
    return ans

def main():
    n,m = list(map(int, input().split()))
    tickets = list(map(int, input().split()))
    customers = list(map(int, input().split()))
    print(*solve(tickets,customers,n,m), sep="\n")

if __name__ == "__main__":
    main()
