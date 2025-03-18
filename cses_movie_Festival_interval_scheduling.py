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

def solve(movies):
    movies.sort(key= lambda movie:movie[1])
    last_finishing_time = -1
    watch_movies = 0

    for movie in movies:
        if movie[0] >= last_finishing_time:
            watch_movies += 1
            last_finishing_time = movie[1]
    return watch_movies


def main():
    movies = []
    n = int(input())
    for _ in range(n):
        movie = list(map(int, input().split()))
        movies.append(movie)
    print(solve(movies))

if __name__ == "__main__":
    main()
