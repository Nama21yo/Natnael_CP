import itertools
from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil, sqrt
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def iinp():
    return int(input().strip())

def linp():
    return list(map(int, input().strip().split()))

def string():
    return input().strip()

def lsinp():
    return input().strip().split()

def digit():
    return [int(i) for i in input().strip()]

def character():
    return list(input().strip())

def equation(mid):
    return (mid*mid) + sqrt(mid)
def solve(c):
    l = 0
    r = c + 1
    # r - l >> 1e10
    # epsilon = 1e-6
    # accuracy log 10^ 16 >> 60
    for i in range(60): # sometimes if it become inaccurate make it 100
        mid = l + (r - l)/2
        possible = equation(mid)
        if possible >= c:
            r = mid
        else:
            l = mid
    return r
def main():
    c = float(input())
    # nums = linp()
    print(solve(c))

if __name__ == '__main__':
    main()

"""
Newton's method
Most simple and accurate way to compute square root is Newton's method.

You have a number which you want to compute its square root (num) and you have a guess of its square root (estimate). Estimate can be any number bigger than 0, but a number that makes sense shortens the recursive call depth significantly.

new_estimate = (estimate + num/estimate) / 2
This line computes a more accurate estimate with those 2 parameters. You can pass new_estimate value to the function and compute another new_estimate which is more accurate than the previous one or you can make a recursive function definition like this.

def newtons_method(num, estimate):
    # Computing a new_estimate
    new_estimate = (estimate + num/estimate) / 2
    print(new_estimate)
    # Base Case: Comparing our estimate with built-in functions value
    if new_estimate == math.sqrt(num):
        return True
    else:
        return newtons_method(num, new_estimate)
For example we need to find 30's square root. We know that the result is between 5 and 6.

newtons_method(30,5)
number is 30 and estimate is 5. The result from each recursive calls are:

5.5
5.477272727272727
5.4772255752546215
5.477225575051661
The last result is the most accurate computation of the square root of number. It is the same value as the built-in function math.sqrt().

"""
"""
Given a positive integer N and a precision factor P, write a square root function that produce an output with a maximum error P from the actual square root of N.


Example:
Given N = 5 and P = 0.001, can produce output O such that 2.235 < O > 2.237. Actual square root of 5 being 2.236.


public static double squareRoot(int N, float P) { 
    double guess = N / 2;
 
    while( Math.abs( guess*guess - N ) > P) {
       guess  = ( guess + (  N / guess ) ) / 2;
    }
    return guess;
}
"""
